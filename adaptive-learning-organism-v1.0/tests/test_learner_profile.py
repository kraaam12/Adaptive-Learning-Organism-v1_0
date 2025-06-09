
from src.learner_profile import LearnerProfile

def test_update_scores():
    lp = LearnerProfile()
    lp.update_scores_v1('high')
    assert 'curiosity' in lp.traits
