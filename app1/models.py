from django.db import models

# Create your models here.

class Bookappoinmenttime(models.Model):

	calendar=models.DateTimeField()

	time=models.CharField(max_length=8)

class Bookappoinment(models.Model):

	Patient_Name =models.CharField(max_length=20)

	PhoneNumber=models.CharField(max_length=10)

	Patient_Cause=models.CharField(max_length=20)

	Patient_Doctor=models.CharField(max_length=15)

	Patient_City=models.CharField(max_length=30)

	Date_Time=models.ForeignKey(Bookappoinmenttime,on_delete=models.CASCADE,default=1,blank='True',null='True')








