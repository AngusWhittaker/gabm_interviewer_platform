from sim_brain.brains.abstract_brain import AbstractBrain
from openai import OpenAI
import json

class ParkBrain(AbstractBrain):
    """A brain implementation based upon Park's study."""
    
    @property
    def model(self):
        return "gpt-4o-mini"
    
    def create_reflection(self, interview, expert_prompt):
        """ Creates the expert reflections"""
        try:
            client = OpenAI()

            messages = [
                {"role": "developer", "content": expert_prompt},
                {"role": "developer", "content": interview}
            ]
            
            print(f"\nSending request to OpenAI for reflection: ...")

            response = client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            print(f"Received response from OpenAI for reflection: {response.choices[0].message.content}")

            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
        return None

    def chat(self, transcript, messages, question, expert_reflections=None):
        """Generates a chat response using an LLM."""
        try:
            client = OpenAI()
            expert = None
            if expert_reflections is not None and len(expert_reflections) > 1:
                expert_name = self._select_expert(question, [reflection.reflectionType.name for reflection in expert_reflections], client)
                expert = expert_reflections.filter(reflectionType__name=expert_name).first()
            elif expert_reflections is not None and len(expert_reflections) == 1:
                expert = expert_reflections[0]

            if expert is not None:
                return self._send_chat_with_expert(transcript, messages, expert, client)
            
            return self._send_chat_without_expert(transcript, messages, client)

        except Exception as e:
            print(f"Error: {e}")
        return None
    
    def _select_expert(self, question, experts, client):
        """Uses the LLM to select the most relevant expert for the given question."""
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
            model=self.model,
            messages=input_messages,
            tools=tools,
        )

        args = json.loads(response.choices[0].message.tool_calls[0].function.arguments)

        if "expert" not in args:
            raise ValueError("No expert selected.")
        if args["expert"] not in experts:
            raise ValueError(f"Selected expert {args['expert']} is not in the list of experts: {experts}")
        return args["expert"]
    
    

    def _send_chat_with_expert(self, transcript, context, expert, client):
        """Sends a chat message with the expert reflection to the LLM and returns the response."""
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

        return self._send_chat(message, context, client)

    def _send_chat_without_expert(self, transcript, context, client):
        """Sends a chat message without any expert reflection to the LLM and returns the response."""
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

        return self._send_chat(message, context, client)
    
    def _send_chat(self, message, context, client):
        """Sends a chat message to the LLM and returns the response."""
        messages = [
            {"role": "user", "content": message}
        ]

        messages.extend(entry for entry in context)

        response = client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return response.choices[0].message.content
