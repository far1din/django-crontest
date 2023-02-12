from django.contrib import admin

from .models import TestJob

class TestJobAdmin(admin.ModelAdmin):
    list_display = ['name', 'iteration', 'created_at']

admin.site.register(TestJob, TestJobAdmin)