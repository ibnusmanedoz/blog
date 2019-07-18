from django.db import models
import datetime
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class TodoData(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    todo_data = models.CharField(max_length=200)
    when = models.DateField()
    time = models.CharField(max_length=7)

    def __str__(self):
        return self.todo_data
