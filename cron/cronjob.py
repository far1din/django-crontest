from .models import TestJob

def AddTestJob():
    last = TestJob.objects.last().iteration
    TestJob.objects.create(name='This is cronjob ' + str(last + 1), iteration=last+1)
    return print(last)