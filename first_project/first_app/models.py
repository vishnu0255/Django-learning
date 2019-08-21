from django.db import models

# Create your models here.
class Test(models.Model):
	sno=models.IntegerField(unique=True)
	name=models.CharField(max_length=50)
	def _str_(self):
		return "hi"
				
class Test1(models.Model):
	sno=models.IntegerField(unique=True)
	def _str_(self):
		return "hi1"
class User(models.Model):
	firstName=models.CharField(max_length=20)
	secondName=models.CharField(max_length=20)
	email=models.CharField(max_length=50)
	def _str_(self):
		return "hi1"