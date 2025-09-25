import pytest
from reviews.services import predict_sentiment


def test_predict_sentiment_smoke():
    lbl, score = predict_sentiment("I loved this movie, it was fantastic!")
    assert lbl in {"Positive", "Negative"}
    assert 0.0 <= score <= 1.0
    
def test_predict_sentiment_posivite1():
    lbl, score = predict_sentiment("I loved this movie, it was fantastic!")
    assert lbl == "Positive"
    assert 0.5 <= score <= 1.0
    
def test_predict_sentiment_posivite2():
    lbl, score = predict_sentiment("Great movie, interesting plot")
    assert lbl == "Positive"
    assert 0.5 <= score <= 1.0
    
def test_predict_sentiment_posivite3():
    lbl, score = predict_sentiment("The plot could be more deep, but overall a great movie")
    assert lbl == "Positive"
    assert 0.5 <= score <= 1.0
    
def test_predict_sentiment_negative1():
    lbl, score = predict_sentiment("Hate the plot, most boring movie all time")
    assert lbl == "Negative"
    assert 0.0 <= score <= 0.5
    
def test_predict_sentiment_negative2():
    lbl, score = predict_sentiment("Total garbage, don't recommend to anyone")
    assert lbl == "Negative"
    assert 0.0 <= score <= 0.5
    
def test_predict_sentiment_negative3():
    lbl, score = predict_sentiment("Who made that costumes? Characters looked like they just ran out of circus...")
    assert lbl == "Negative"
    assert 0.0 <= score <= 0.5
    
def test_predict_sentiment_mixed1():
    lbl, score = predict_sentiment("It had its moments, but overall it wasn't interesting really")
    assert lbl in ["Positive", "Negative"]
    assert 0.35 <= score <= 0.65
    
def test_predict_sentiment_mixed2():
    lbl, score = predict_sentiment("I have mixed feelings, I liked the characters, but plot was too shallow")
    assert lbl in ["Positive", "Negative"]
    assert 0.35 <= score <= 0.65
