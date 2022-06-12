from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField()

    def __str__(self):
        return f'{self.roll_no}---{self.first_name}---{self.last_name}---{self.mail}'

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_fees = models.FloatField()

    def __str__(self):
        return f'{self.student}---{self.course_name}---{self.course_fees}'

