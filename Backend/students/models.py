from django.db import models

# Create your models here.
class students(models.Model):
    name = models.TextField()
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
