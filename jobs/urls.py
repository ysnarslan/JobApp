from django.urls import path
from .views import *

urlpatterns = [
    path("", job_list, name='index'),
    path("job/<int:id>", job_detail, name='job_detail'),
    path("hello/", hello, name='hello')
]
