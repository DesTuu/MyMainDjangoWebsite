from django.shortcuts import render

from django.http import HttpResponse

# programming = ("Python", "JavaScript", "Java", "C#")


# def home(request):
#     return HttpResponse("Welcome Home")

def home(request):
    return render(request, 'my_app/home.html')
