from django.db import models

# Create your models here.
class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Person_ID:{self.pid}---First_Name:{self.first_name}---Last_Name:{self.last_name}'

class Adhar(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    aid = models.IntegerField()

    def __str__(self):
        return f'Person:{self.person}---Adhar_Id:{self.aid}'