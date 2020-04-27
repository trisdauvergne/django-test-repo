# from Django shortcuts import render
from django.http import HttpResponse


def landing_page(request):
    return HttpResponse('Well, this is my response to your request!')


def another_page(request):
    return HttpResponse('This is the response for that url!')
