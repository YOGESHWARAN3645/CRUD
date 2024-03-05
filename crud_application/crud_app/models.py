from django.db import models

class UserTable(models.Model):
    emp_name=models.CharField(max_length=200)
    emp_id= models.IntegerField()

# Create your models here.
