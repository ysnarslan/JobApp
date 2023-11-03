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
    list_of_jobs = "<lu>"
    for job in job_title:
        job_id = job_title.index(job) + 1
        job_detail_url = reverse('job_detail', args=(job_id,))
        list_of_jobs += f"<li> <a href='{job_detail_url}'> {job} </a> </li>"

    list_of_jobs += "</lu>"
    return HttpResponse(list_of_jobs)


def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('home'))

        idx = id - 1
        return_html = f"<h1>{job_title[idx]}</h1> <h3> {job_description[idx]}"
        return HttpResponse(return_html)

    except:
        return HttpResponseNotFound('Not Found')
