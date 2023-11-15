from django.shortcuts import render, HttpResponse
from datetime import datetime





def title_page(request):

    if request.method == 'GET':
        return render(request, 'index.html')


def hello_world(request):

    #return HttpResponse("Hello Bruh! What's up ?")
    if request.method == 'GET':
        return render(request, 'hello.html')


def current_date(request):
    now = datetime.now()
    context = {
        'current_date': now.strftime("%Y-%m-%d"),
        'current_time': now.strftime("%H:%M:%S"),
    }
    if request.method == 'GET':
        return render(request, 'current_date.html', context)


def goodby (request):
    if request.method == 'GET':
        return render(request, 'goodby.html')
