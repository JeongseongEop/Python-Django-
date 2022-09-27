from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    """
    Example 목록출력
    
    """
    question_list = Question.objects.order_by('create_date')
    context = {'question_list' : question_list}
    return render (request, 'Example/question_list.html', context)



def detail(request, question_id):
    """
    Example 내용출력
    """
    question = Question.objects.get(id=question_id)
    context = {' question ' : question }
    return render( request, 'Example/question_detail.html', context)
