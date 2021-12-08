from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quiz(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.description}"

    def get_questions(self):
        return f"{self.questions.all()}"

    class Meta:
        verbose_name_plural = 'Тест'


class Question(models.Model):
    question = models.CharField(max_length=10000)
    type = models.CharField(max_length=300)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return f"{self.question}"

    def get_answers(self):
        return f"{self.answers.all()}"

    class Meta:
        verbose_name_plural = 'Питання'

class Answer(models.Model):
    options = models.CharField(max_length=10000)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return f"{self.options}"

    class Meta:
        verbose_name_plural = 'Відповіді'

class UsersAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)