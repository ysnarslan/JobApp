from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Job(models.Model):
    job_title = models.CharField(
        max_length=255,
        help_text="",
    )
    job_description = models.TextField(
        help_text="",
    )
    created_date = models.DateField(
        auto_now_add=True,
        help_text="",
    )
    salary = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="",
    )
