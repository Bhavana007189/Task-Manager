from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=10)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
