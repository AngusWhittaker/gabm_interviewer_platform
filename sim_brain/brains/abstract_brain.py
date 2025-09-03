from abc import ABC, abstractmethod

class AbstractBrain(ABC):
    """Abstract base class for different brain implementations."""

    @abstractmethod
    def create_reflection(self, interview, expert_prompt):
        """Creates the expert reflections using an LLM."""
        pass

    @abstractmethod
    def chat(self, transcript, messages, question, expert_reflections=None):
        """Generates a chat response using an LLM."""
        pass

    @property
    @abstractmethod
    def model(self):
        """The LLM model used."""
        pass