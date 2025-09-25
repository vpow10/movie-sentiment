from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib, json, time, os
from pathlib import Path


HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "model.joblib"
META = HERE / "metadata.json"


print("Loading IMDB dataset...")
ds = load_dataset("imdb")
X = ds["train"]["text"][:] + ds["test"]["text"][:]
y = ds["train"]["label"][:] + ds["test"]["label"][:]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=47, stratify=y)

clf = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), min_df=2, max_df=0.9)),
    ("lr", LogisticRegression(max_iter=1000, n_jobs=-1))
])

start = time.time()
clf.fit(X_train, y_train)
elapsed = time.time() - start

pred = clf.predict(X_val)
acc = accuracy_score(y_val, pred)
report = classification_report(y_val, pred, output_dict=True)
print(f"Validation accuracy: {acc:.4f}")

ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(clf, ARTIFACT)
META.write_text(json.dumps({
    "accuracy": acc,
    "elapsed_sec": elapsed,
    "classes": {"0": "negative", "1": "positive"},
}, indent=2))
print(f"Saved model -> {ARTIFACT}")
