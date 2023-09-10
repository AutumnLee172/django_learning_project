from django.db import models

class User(models.Model):
  email = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_date = models.DateTimeField(null=True, blank=True)
# Create your models here.
