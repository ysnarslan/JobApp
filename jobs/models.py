from django.db import models


# Create your models here.
class Job(models.Model):
    job_title = models.CharField(
        max_length=255,
        help_text="",
    )
