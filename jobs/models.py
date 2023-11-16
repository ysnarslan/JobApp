from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.


class Location(models.Model):
    street = models.CharField(
        max_length=255,
        help_text="",
    )
    city = models.CharField(
        max_length=255,
        help_text="",
    )
    state = models.CharField(
        max_length=255,
        help_text="",
    )
    country = models.CharField(
        max_length=255,
        help_text="",
    )
    zip = models.CharField(
        max_length=255,
        help_text="",
    )


class Author(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="",
    )
    company = models.CharField(
        max_length=255,
        help_text="",
    )
    designation = models.CharField(
        max_length=255,
        help_text="",
    )


class Skill(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="",
    )


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
    ]
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
    slug = models.SlugField(
        null=True,
        unique=True,
        max_length=40,
    )
    expiry = models.DateField(
        null=True,
    )
    location = models.OneToOneField(
        Location,
        null=True,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        null=True,
    )
    skill = models.ManyToManyField(
        to=Skill,
    )
    job_type = models.CharField(
        choices=JOB_TYPE_CHOICES,
        max_length=255,
        null=False,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.job_title)

        return super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.job_title
