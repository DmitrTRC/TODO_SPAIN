from django.db import models
from django.utils import timezone
import datetime


class Todo(models.Model):
    text = models.CharField(max_length=80)
    deadline_time = models.DateTimeField(verbose_name='Deadline', blank=True, default=timezone.now)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def is_week_old(self):
        return self.deadline_time >= (timezone.now() - datetime.timedelta(days=7))

    def is_month_old(self):
        return self.deadline_time >= (timezone.now() - datetime.timedelta(days=30))
