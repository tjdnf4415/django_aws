from django.shortcuts import render
from myapp import models


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'myapp/question_list.html', context)