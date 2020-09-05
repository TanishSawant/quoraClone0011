from django.shortcuts import render
from .models import Questions, Answers
from django.http import HttpResponse

# Create your views here.

def questionListView(request, *args, **kwargs):
    questionList = Questions.objects.all()
    context = {
        'listObject' : questionList
    }
    return render(request, 'questionList.html', context)