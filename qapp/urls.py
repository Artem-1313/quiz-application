from . import views
from django.urls import path, include
from .views import QuizList, QuizDetail

urlpatterns = [
    path('', QuizList.as_view(), name="quizzes"),
    path('<int:pk>/', QuizDetail.as_view(), name="quiz-detail"),
]