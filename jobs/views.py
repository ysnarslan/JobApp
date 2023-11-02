from django.http import HttpResponse
from django.shortcuts import render


job_title = [
    'First Job',
    'Second Job'
]
job_description = [
    'First job description.',
    'Second job description.'
]

# Create your views here.
def hello(request):
    return HttpResponse('<h3>Hello World!</h3>')


def job_detail(request, id):
    idx = int(id) - 1
    return_html = f"<h1>{job_title[idx]}</h1> <h3> {job_description[idx]}"

    return HttpResponse(return_html)

