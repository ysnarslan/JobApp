from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse('<h3>Hello World!<h3>')


def job_detail(request, id):
    site = "https://google.com"

    return HttpResponse(f"Visit Google from <a href={site} target='_blank'> here <a> ")

