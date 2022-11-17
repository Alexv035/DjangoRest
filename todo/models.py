from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    notes = models.CharField(max_length=64)
    date_creation = models.DateField()
    date_update = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    actives = models.BooleanField()

    def __str__(self):
        return self.name
