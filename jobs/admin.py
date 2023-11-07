from django.contrib import admin
from jobs.models import Job


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ["id", "job_title", "job_description", "salary", "created_date"]
    list_filter = ["salary", "created_date", "expiry"]
    # list_editable = []
    search_fields = ["job_title", "salary", "job_description"]
    search_help_text = "Write in your query and hit search"
    # fields = ["job_title", "job_description", "salary"]
    # exclude = []
    fieldsets = (
        ("Basic info", {
            "fields": ["job_title", "job_description"]
        }),
        ("More info", {
            "fields": ["expiry", "salary", "slug"],
            "classes": ["collapse"],
        }),
    )

    class Meta:
        model = Job


admin.site.register(Job, JobAdmin)
