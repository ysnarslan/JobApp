from django.urls import path
from .views import *

urlpatterns = [
    path("", job_list),
    path("job/<int:id>", job_detail)
]
