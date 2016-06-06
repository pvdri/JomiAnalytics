from __future__ import unicode_literals

from django.db import models

# Create your models here.
class analytics(models.Model):
    si = models.URLField(max_length=128, unique=True)
    ip = models.CharField(max_length=128)
    org = models.CharField(max_length=128)
    time = models.CharField(max_length=128)
    timep = models.CharField(max_length=128)
    geol = models.CharField(max_length=128)

class jcanalytics(models.Model):
    org = models.CharField(max_length=128, unique=True)
