from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import addQuiz
from django.views.generic import ListView, DetailView
from .models import *
from django.http import JsonResponse


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
            questions_list.append({str(q): answers})

        # print("request is", self.request.POST)
        context['dict_questions_answers'] = questions_list
        return context


def test(request):
    dict = request.POST
    dict._mutable = True
    dict.pop('csrfmiddlewaretoken')
    # print(dict)
    result = []
    for k, v in dict.items():
        if v == "":
            result.append({k: "not answer"})
            continue

        for q in Question.objects.filter(question=k):
            for i in q.get_right_answer():
                if str(i) == v:
                    result.append({q.question: {"is right": True, "answer": v}})
                else:
                    result.append({q.question: {"is right": False, "answer": v}})
    print(result)
    return JsonResponse({"test": result})
