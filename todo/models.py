from django.db import models

# Create your models here.


class Project(models.Model):
    notes = models.CharField(max_length=64)
    date_creation = models.DateField()
    date_update = models.DateField()
    user = models.CharField(max_length=64)
    actives = models.BooleanField()
