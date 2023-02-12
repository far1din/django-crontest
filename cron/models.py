from django.db import models

class TestJob(models.Model):
    name = models.CharField(max_length=97, null=False)
    iteration = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
