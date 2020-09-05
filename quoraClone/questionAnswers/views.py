from django.shortcuts import render, get_object_or_404
from .models import Questions, Answers
from django.http import HttpResponse


# Create your views here.

def questionListView(request, *args, **kwargs):
    questionList = Questions.objects.all()
    print(questionList)
    context = {
        'listObject' : questionList
    }
    return render(request, 'questionList.html', context)

def questionDetailView(request, q_id ,*args, **kwargs):
    question = get_object_or_404(Questions, id = q_id)
    _list = [question]
    context = {
        'object' : _list
    }
    return render(request, 'questionDetails.html', context)