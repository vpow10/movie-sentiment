from django.db import models


class Review(models.Model):
    text = models.TextField()
    predicted_label = models.CharField(max_length=16)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.predicted_label} ({self.score:.2f})"
