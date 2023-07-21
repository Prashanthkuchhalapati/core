from django.shortcuts import render

from django.http import HttpResponse



def home(request):

    peoples = [
        {'name' : 'ram','age' : 26},
        {'name' : 'ragu','age': 44},
        {'name' : 'bheem','age' : 35},
        {'name' : 'jeev','age': 43},
        {'name' : 'dev','age' : 29},
        {'name' : 'neet','age': 47},
    ]
    
        
    return render(request , "index.html", context = {'peoples' : peoples})


def success_page(request):
    return HttpResponse("<h1>Hey i successfully created a apage</h1>")