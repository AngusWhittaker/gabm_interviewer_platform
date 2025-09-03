from sim_brain.brains import ParkBrain, DopplegangerBrain

class BrainFactory():
    """Factory class to create brain instances."""
    brains = {
        "park": ParkBrain,
        "doppleganger": DopplegangerBrain
    }

    @classmethod
    def create_brain(cls, brain: str):
        """Create a brain instance based on the given brain type."""
        return cls.brains[brain.lower()]()

    @classmethod
    def get_available_brains(cls):
        """Get a list of available brain types."""
        return list(cls.brains.keys())