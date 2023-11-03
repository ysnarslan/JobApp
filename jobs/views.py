from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

job_title = [
    'First Job',
    'Second Job',
    'Third Job'
]
job_description = [
    'First job description.',
    'Second job description.',
    'Third job description.'
]


# Create your views here.


class TempClass:
    x = 5


def hello(request):
    first_list = ["alpha", "beta"]
    temp = TempClass()
    context = {'name': 'Yasin',
               'first_list': first_list,
               'temp_object': temp,
               'age': 10,
               'is_authenticated': True,
               }
    return render(request, 'jobs/hello.html', context)


def job_list(request):

    context = {
        'job_title': job_title,
    }
    return render(request, 'jobs/index.html', context)


def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('home'))

        idx = id - 1
        context = {
            'job_title': job_title[idx],
            'job_description': job_description[idx],
        }
        return render(request, 'jobs/job_detail.html', context)

    except:
        return HttpResponseNotFound('Not Found')
