from django.db import models

# Create your models here.
class registeronline(models.Model):
	name = models.CharField(max_length=300)
	lastname = models.CharField(max_length=300)
	ci = models.IntegerField()
	phone = models.IntegerField()
	email = models.CharField(max_length=300)
	course = models.CharField(max_length=300)
	contact = models.CharField(max_length=300)
