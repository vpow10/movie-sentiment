from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(
        label="Paste your movie review",
        widget=forms.Textarea(
            attrs={"rows": 6, "placeholder": "I loved the acting..."}
        ),
        min_length=10,
        max_length=5000,
    )
