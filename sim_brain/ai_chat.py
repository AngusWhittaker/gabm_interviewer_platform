from openai import OpenAI
import json

def ai_response(transcript, messages, question, expert_reflections=None):
    """ Creates the expert reflections using OpenAI's API."""
    try:
        client = OpenAI()
        expert = None
        if expert_reflections is not None and len(expert_reflections) > 1:
            expert_name = select_expert(question, [reflection.reflectionType.name for reflection in expert_reflections], client)
            expert = expert_reflections.filter(reflectionType__name=expert_name).first()
        elif expert_reflections is not None and len(expert_reflections) == 1:
            expert = expert_reflections[0]

        if expert is not None:
            return send_chat_with_expert(transcript, messages, expert, client)
        
        return send_chat_without_expert(transcript, messages, client)

    except Exception as e:
        print(f"Error: {e}")
    return None

def select_expert(question, experts, client):
    """Uses OpenAI to select the most relevant expert for the given question."""
    tools = [{
        "type": "function",
        "function": {
            "name": "retrieve_selected_expert",
            "description": "Returns the selected expert.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expert": {
                        "type": "string",
                        "enum": experts,
                        "description": "The selected expert.",
                    }
                },
                "required": [
                    "expert"
                ],
                "additionalProperties": False
            } 
        },
        "strict": True
    }]

    message = f"Please select the domain expert insight that would be most useful for the following question: {question}."

    input_messages = [{"role": "user", "content": message}]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=input_messages,
        tools=tools,
    )

    args = json.loads(response.choices[0].message.tool_calls[0].function.arguments)

    if "expert" not in args:
        raise ValueError("No expert selected.")
    if args["expert"] not in experts:
        raise ValueError(f"Selected expert {args['expert']} is not in the list of experts: {experts}")
    return args["expert"]

def send_chat_with_expert(transcript, context, expert, client):
    message = f"""Participant's interview transcript: {transcript}\n
    Expert reflection: {expert.content}\n
    ============================\n
    Task: What you see above is an interview transcript and the {expert.reflectionType.name}'s reflection on the transcript. 
    Based on the interview transcript, I want you to predict the participant's response in the following conversation. 
    
    As you answer, I want you to take the following steps:
    Step 1) Identify and describe in a few sentences the possible response options and what 
    kind of person would choose each of the response options. ("Option Interpretation")
    Step 2) For each response option, reason about why the
    Participant might answer with that particular option. ("Option
    Choice")
    Step 3) Write a few sentences reasoning on which of these options
    best predicts the participant's response. ("Reasoning")
    Step 4) Predict how the participant will actually respond in the
    following conversation. Predict based on the interview and your thoughts.
    ("Response")"""

    return send_chat(message, context, client)

def send_chat_without_expert(transcript, context, client):
    message = f"""Participant's interview transcript: {transcript}\n
    ============================\n
    Task: What you see above is an interview transcript. 
    Based on the interview transcript, I want you to predict the participant's response in the following conversation. 
    
    As you answer, I want you to take the following steps:
    Step 1) Identify and describe in a few sentences the possible response options and what 
    kind of person would choose each of the response options. ("Option Interpretation")
    Step 2) For each response option, reason about why the
    Participant might answer with that particular option. ("Option
    Choice")
    Step 3) Write a few sentences reasoning on which of these options
    best predicts the participant's response. ("Reasoning")
    Step 4) Predict how the participant will actually respond in the
    following conversation. Predict based on the interview and your thoughts.
    ("Response")"""

    return send_chat(message, context, client)

def send_chat(message, context, client):

    messages = [
        {"role": "user", "content": message}
    ]

    messages.extend(entry for entry in context)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content