from django.db import models

class SentimentAnalysis(models.Model):
    user_input = models.TextField()
    sentiment_score = models.FloatField()
    sentiment_label = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input
