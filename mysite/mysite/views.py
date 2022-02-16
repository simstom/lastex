from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# def index(request):
#     return HttpResponse("절대적인 내용을로 접속이 되었는가요. 절말로")

def index(request):
    
    context = {'latest_question_listaaa': 123}
    return render(request, 'mysite/index.html', context)