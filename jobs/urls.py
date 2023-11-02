from django.urls import path
from .views import *

urlpatterns = [
    path("", hello),
    path("job/<id>", job_detail)
]
