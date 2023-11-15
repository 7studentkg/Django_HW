from django.shortcuts import render, HttpResponse


def hello_world(request):

    #return HttpResponse("Hello Bruh! What's up ?")
    if request.method == 'GET':
        return render(request, 'index.html')
