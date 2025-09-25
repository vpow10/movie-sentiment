# Movie Review Sentiment Analyzer

A small Django web app that predicts whether a movie review is **Positive** or **Negative**.

## How it works

- **Home page (`/`)** shows a textarea and an **Analyze** button.
- When you submit a review, the page uses **htmx** to POST to **`/predict/`** without a full reload.
- The server runs the review through a saved **scikit‑learn** model (TF‑IDF + Logistic Regression) and returns:
  - **Label**: Positive / Negative
  - **Score**: 0.00–1.00
- The app stores each analysis (text, label, score, timestamp) in **SQLite** and shows the last few results on the right.
- Templates use **Bootstrap 5** for simple styling.

### Files worth knowing
- `reviews/ml/train_model.py` — trains the model on the IMDB dataset and saves it to `reviews/ml/model.joblib`.
- `reviews/services.py` — loads the saved model and makes predictions.
- `reviews/views.py` — handles the home page and the `/predict/` endpoint.
- `reviews/templates/` — HTML templates (`index.html`, `_result.html`, `base.html`).

## Run locally

> Requires Python 3.10+ and a working internet connection the first time you train (to download the IMDB dataset).

```bash
# 1) Clone & enter
git clone <your-repo-url> movie-sentiment
cd movie-sentiment

# 2) Create & activate a virtual environment
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Train the model (creates reviews/ml/model.joblib)
python reviews/ml/train_model.py

# 5) Prepare the database
python manage.py migrate

# 6) Start the server
python manage.py runserver
# open http://127.0.0.1:8000
```

## Endpoints

- `GET /` — Home page with form and recent analyses.
- `POST /predict/` — Accepts form data (`text`) and returns the result partial HTML (used by htmx).

## Troubleshooting

- **`FileNotFoundError: model.joblib`** → Run `python reviews/ml/train_model.py` first.
- **Dataset download issues** → Check your internet connection and retry `train_model.py`.
- **Windows PowerShell execution policy** (activating venv) → Run PowerShell as admin and `Set-ExecutionPolicy RemoteSigned` (if needed).

## Notes

- The model artifact `reviews/ml/model.joblib` is generated locally and typically excluded from Git.
- All inference runs locally; the app does not call external APIs at runtime.
