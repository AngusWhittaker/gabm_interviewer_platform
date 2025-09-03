from sim_brain.brains.abstract_brain import AbstractBrain
from openai import OpenAI
import json

class DopplegangerBrain(AbstractBrain):
    """A brain implementation that focuses on imitating the user's behavior."""
    
    @property
    def model(self):
        return "gpt-4o-mini"
    
    def create_reflection(self, interview, expert_prompt):
        """Creates the expert reflections"""
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
            message = f"""Participant's interview transcript: {transcript}\n
            ============================\n
            Task: What you see above is an interview transcript. 
            Based on the interview transcript, I want you to predict the Participant's response in the following conversation and behave like them. 
            
            As you answer, I want you to silently consider the following steps in your mind:
            Step 1) Identify the possible response options that you predict the Participant might take based upon their interview transcript, perceived personality traits and response style.
            Step 2) Identify what kind of person would choose each of the response options.
            Step 3) For each response option, reason about why the Participant might answer with that particular option.
            Step 4) Reason on which of these options best predicts the Participant's response.
            Step 5) Predict how the Participant will actually respond in the following conversation. Predict based on the interview and your thoughts.

            Once you have predicted how the participant will respond return only that predicted response. Do not provide your reasoning."""
            
            messagesToSend = [
                {"role": "user", "content": message}
            ]

            messagesToSend.extend(entry for entry in messages)

            response = client.chat.completions.create(
                model=self.model,
                messages=messagesToSend
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"Error: {e}")
        return None
