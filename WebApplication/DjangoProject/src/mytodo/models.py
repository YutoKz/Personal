from django.db import models

# Create your models here.


class Task(models.Model):
    doing = 0
    done = 1
    TASK_STATUS_CHOICES = [
        (doing,'進行中'),
        (done,'完了'),
    ]
    title = models.CharField(max_length=50)
    body = models.TextField()
    status =models.IntegerField(default=0,choices=TASK_STATUS_CHOICES)

