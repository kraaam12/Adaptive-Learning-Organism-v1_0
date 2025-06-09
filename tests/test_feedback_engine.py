
from src.feedback_engine import apply_feedback

def test_apply_feedback():
    result = apply_feedback({'curiosity': 0.5}, 'medium')
    assert isinstance(result, dict)
