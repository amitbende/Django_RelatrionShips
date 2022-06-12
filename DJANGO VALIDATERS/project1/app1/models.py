from django.db import models

# Create your models here.
class Employees(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    salary = models.FloatField()
    password = models.CharField(max_length=30)
    c_password = models.CharField(max_length=30)

