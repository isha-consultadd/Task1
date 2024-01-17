from django.db import models

class Employee(models.Model):
    employeeid = models.CharField(max_length=100)
    employeename = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)



