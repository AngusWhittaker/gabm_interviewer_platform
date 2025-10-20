from sim_brain.brains.abstract_brain import AbstractBrain

class SillyBrain(AbstractBrain):
    """A silly brain implementation that swaps your words around."""
    
    @property
    def model(self):
        return None
    
    def create_reflection(self, interview, expert_prompt):
        return ""
    
    def chat(self, transcript, messages, question, expert_reflections=None):
        """Returns the message with words swapped around."""
        question_words = question.split()
        swapped_words = question_words[::-1]
        return " ".join(swapped_words)