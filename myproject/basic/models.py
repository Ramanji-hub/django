from django.db import models
import uuid


# Create your models here.
class userprofile(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    city=models.CharField(max_length=100)

class Employee(models.Model):
    emp_name=models.CharField(max_length=150)
    emp_salary=models.IntegerField()
    emp_email=models.EmailField(unique=True)

class MovieBooking(models.Model):
    moviename=models.CharField(max_length=100)
    showtime=models.CharField(max_length=100)
    screenname=models.CharField(max_length=100)
    dateandtime=models.DateTimeField(auto_now_add=True)
    transaction_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)