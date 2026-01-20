def score_output(text: str) -> float:
    # Simple heuristic score
    return min(len(text) / 50.0, 1.0)