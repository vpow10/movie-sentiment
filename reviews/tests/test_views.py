import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_ok(client):
    resp = client.get(reverse("index"))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_predict_ok(client):
    resp = client.post(reverse("predict"), {"text": "Great acting and direction."})
    assert resp.status_code == 200
    assert b"Positive" in resp.content or b"Negative" in resp.content
