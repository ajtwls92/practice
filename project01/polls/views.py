from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from polls.models import Question

def index(request):
    #return HttpResponse("polls Index.")
    question_list = Question.objects.all()\
        .order_by('-pub_date')[:5]
    context = {'question_list':question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse('polls detail.')
    question = Question.objects.get(id=question_id)
    
    return render(request, 
                    'polls/detail.html', 
                    {'question':question})

def vote(request, question_id):
    #return HttpResponse('polls vote.')
    q = Question.objects.get(pk=question_id)
    choice_id = request.POST['choice']
    selected_choice = q.choice_set.get(pk=choice_id)
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(f'/polls/{q.id}/result/')

def result(request, question_id):
    #return HttpResponse('polls result.')
    q = Question.objects.get(pk=question_id)
    return render(request, 'polls/result.html', {'q':q})