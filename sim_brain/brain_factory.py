from sim_brain.brains import ParkBrain, DopplegangerBrain

def BrainFactory(brain: str):
    """Factory method to create brain instances."""
    brains = {
        "park": ParkBrain,
        "doppleganger": DopplegangerBrain
    }

    return brains[brain.lower()]()