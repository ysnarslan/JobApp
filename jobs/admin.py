from django.contrib import admin
from jobs.models import Job


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ["id", "job_title", "salary", "created_date"]
    # list_editable = []
    # search_fields = []

    class Meta:
        model = Job


admin.site.register(Job, JobAdmin)
