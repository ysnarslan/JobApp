from django.urls import path
from uploadpp.views import upload_pp, upload_file

urlpatterns = [
    path('image/', upload_pp, name='upload_pp'),
    path('file/', upload_file, name='upload_file'),
]
