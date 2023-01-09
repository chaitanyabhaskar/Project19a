import email
from pyexpat import model
from django.db import models
from django.forms import IntegerField

# Create your models here.
class table1(models.Model):
    email = models.CharField(max_length=100)
    passw = models.IntegerField()
class staff(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
class ExamDetails(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    dt = models.DateField()
class ChangesDetails(models.Model):
    Date = models.DateField()
    Id = models.CharField(max_length=100)
    RId= models.CharField(max_length=100)