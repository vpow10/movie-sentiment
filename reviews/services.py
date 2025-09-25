from functools import lru_cache
from pathlib import Path

import joblib


@lru_cache(maxsize=1)
def _load_model():
    path = Path(__file__).resolve().parent / "ml" / "model.joblib"
    if not path.exists():
        raise FileNotFoundError(
            "Model artifact not found. Run reviews/ml/train_model.py"
        )
    return joblib.load(path)


LABELS = {0: "Negative", 1: "Positive"}


def predict_sentiment(text: str) -> tuple[str, float]:
    model = _load_model()
    proba = model.predict_proba([text])[0]
    print(proba)
    score_pos = float(proba[1])
    label = LABELS[1 if score_pos >= 0.5 else 0]
    return label, score_pos
