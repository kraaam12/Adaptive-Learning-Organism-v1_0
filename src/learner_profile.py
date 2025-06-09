
from src.feedback_engine import apply_feedback

class LearnerProfile:
    def __init__(self):
        self.traits = {'curiosity': 0.5, 'resilience': 0.5}

    def update_scores_v1(self, feedback_level):
        self.traits = apply_feedback(self.traits, feedback_level)
