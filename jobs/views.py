from django.http import HttpResponse

from django.shortcuts import render, redirect

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
def job_list(request):
    list_of_jobs = "<lu>"
    for job in job_title:
        job_id = job_title.index(job) + 1
        list_of_jobs += f"<li> <a href='job/{job_id}'> {job} </a> </li>"

    list_of_jobs += "</lu>"
    return HttpResponse(list_of_jobs)


def job_detail(request, id):
    if id == 0:
        return redirect("/")
    idx = id - 1
    return_html = f"<h1>{job_title[idx]}</h1> <h3> {job_description[idx]}"

    return HttpResponse(return_html)
