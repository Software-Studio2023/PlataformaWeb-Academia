from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class students(AbstractBaseUser):
    name = models.TextField()
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    password = models.CharField(max_length=200,  blank=True, null=True)
