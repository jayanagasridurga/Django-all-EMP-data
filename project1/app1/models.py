from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=60)
    Emp_Id=models.IntegerField()
    Desi=models.CharField(max_length=50)
    Location=models.CharField(max_length=60)
    def __str__(self):
        return self.Name
