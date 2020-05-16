from django.db import models

# Create your models here.
class InfoModel(models.Model):
    memo = models.TextField()