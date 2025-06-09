
from src import config

def apply_feedback(trait_scores, feedback_level):
    delta = config.SCORE_DELTA_CURVE.get(feedback_level, 0.1)
    return {
        trait: score * config.DECAY_FACTOR + delta * config.REINFORCEMENT_WEIGHT
        for trait, score in trait_scores.items()
    }
