from openai import OpenAI

def create_reflection(interview, expert_prompt):
    """ Creates the expert reflections using OpenAI's API."""
    try:
        client = OpenAI()

        messages = [
            {"role": "developer", "content": expert_prompt},
            {"role": "developer", "content": interview}
        ]
        
        print(f"\nSending request to OpenAI for reflection: ...")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        print(f"Received response from OpenAI for reflection: {response.choices[0].message.content}")

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
    return None