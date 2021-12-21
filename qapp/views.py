from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
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

    print(dict)

    result = []
    score = 0
    for question, answers in dict.items():

#question=question[:(len(question)-2)]
        for q in Question.objects.filter(question=question[:(len(question)-2)]):
            q_=question[:(len(question)-2)]
            correct_ans = q.get_right_answer()
            correct_ans_ = set(correct_ans)
            ans = dict.getlist(question)
            if '' in ans and len(ans)>1:
                ans = ans[1:]
            ans_ = set(ans)
            print(ans_-correct_ans_)

            if '' in ans:
                result.append({q_: {"not_answer": True, "correct_ans": correct_ans}})
                continue

            if not (correct_ans_.symmetric_difference(ans_)):
                    score += 1
                    result.append({q_: {"is_right": True, "answer": ans,  "correct_ans":correct_ans,"score":score}})

            else:
                    result.append({q_: {"is_right": False, "answer": ans, "correct_ans": correct_ans }})

    print(result)
    return JsonResponse({"test": result})
