# polls/views.py

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

def index(request):
    latest = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = { 'latest_list': latest }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': q} )


def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
