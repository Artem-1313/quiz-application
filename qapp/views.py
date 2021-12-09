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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        quiz = Quiz.objects.get(id=self.kwargs['pk'])
        questions_list = []
        for q in quiz.get_questions():
        	answers = []
        	for a in q.get_answers():
        		answers.append(str(a))
        	questions_list.append({str(q):answers})

        context['dict_questions_answers'] = questions_list
        return context
def index(request):


    return render(request,  "qapp/index.html")
