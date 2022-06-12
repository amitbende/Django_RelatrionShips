from django.db import models

# Create your models here.
class Owner(models.Model):
    oid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.oid}---{self.first_name}---{self.last_name}'

class Car(models.Model):
    owner = models.ManyToManyField(Owner)
    cid = models.IntegerField(primary_key=True)
    year = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cid}---{self.year}---{self.brand}---{self.model}'

