from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json

# def index(request):
#     return HttpResponse("절대적인 내용을로 접속이 되었는가요. 절말로")


@csrf_exempt
def index_chatbot(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        output = dict()
        output['response'] = "이건 응답"
        return HttpResponse(json.dumps(output), status=200)
    else:
        return render(request, 'chatbot/chat_test.html')