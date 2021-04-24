from django.db import models
from phone_field import PhoneField

# Create your models here.
class Helps(models.Model):
    name = models.CharField(max_length=1000,default="")
    helps = models.CharField(max_length=1000,default="")
    city = models.CharField(max_length=1000,default="")
    state = models.CharField(max_length=1000,default="")
    contact = models.CharField(max_length=1000,default="")
    def __str__(self):
        return f'{self.name} , {self.helps}'
