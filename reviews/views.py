from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review
from .services import predict_sentiment


def index(request: HttpRequest) -> HttpResponse:
    form = ReviewForm()
    recent = Review.objects.all()[:5]
    return render(request, "reviews/index.html", {"form": form, "recent": recent})


def predict(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        form = ReviewForm()
        return render(
            request,
            "reviews/_result.html",
            {"error": "POST a review to analyze.", "form": form},
        )

    form = ReviewForm(request.POST)
    if not form.is_valid():
        return render(request, "reviews/_result.html", {"form": form})

    text = form.cleaned_data["text"]
    label, score = predict_sentiment(text)
    Review.objects.create(text=text, predicted_label=label, score=score)
    context = {"label": label, "score": score}
    return render(request, "reviews/_result.html", context)
