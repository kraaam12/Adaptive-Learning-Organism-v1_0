
from src.learner_profile import LearnerProfile

def run_simulation():
    profile = LearnerProfile()
    print("Initial traits:", profile.traits)
    profile.update_scores_v1('medium')
    print("Updated traits:", profile.traits)
