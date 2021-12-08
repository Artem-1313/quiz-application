from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import addQuiz
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class QuizList(ListView):
    model = Quiz
    template_name = "qapp/index.html"

    def get_queryset(self):
        return Quiz.objects.all()

class QuizDetail(DetailView):
    model = Quiz

def index(request):


    return render(request,  "qapp/index.html")
