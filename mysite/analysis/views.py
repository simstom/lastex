from re import T
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice
from .scrap_s import Scrap

# Create your views here.

# def index_analysis(request):
#     return HttpResponse("접속이 되었는가요.")

# def index_analysis(request):
#     scrap = Scrap()
#     sum = 0
    
#     if sum < 5:
#         html_str = scrap.scrap(True)
#         print(html_str)
#     sum += 1
#     return HttpResponse("%d 접속이 되었는가요. %s"%(sum, html_str))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index_analysis(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # context = {'latest_question_listaaa': latest_question_list}
#     context = {"value":1234567}
#     return render(request, 'analysis/index_analysis.html', context)


def index_analysis(request):
    scrap = Scrap()
    sum = 0
    
    if sum < 5:
        html_str = scrap.scrap(True)
        print(html_str)
    sum += 1
    # html_str = "abcdef-fjfjfjfjfj"
    context = {"value":1234567, "html_value": html_str}
    context = {"context": context}
    return render(request, 'analysis/index_analysis.html', context)

# class BookListView(generic.ListView):
#     model = Book
#     context_object_name = 'my_book_list'   # your own name for the list as a template variable
#     queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
#     template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




