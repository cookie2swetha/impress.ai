from django.db import models

class ChatbotUser(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    question_id = models.IntegerField(default=0)
    answer = models.TextField()

    def __str__(self):
        return f"{self.user_id} - Question {self.question_id}"
