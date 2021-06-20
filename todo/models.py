from django.db import models

# Create your models here.
class ToDo(models.Model):
    content = models.CharField(max_length = 100)
    completed = models.BooleanField(default = False)
    timeCreated = models.DateTimeField(auto_now = True)
