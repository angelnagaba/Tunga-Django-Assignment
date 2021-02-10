from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class profiles(models.Model):
    name = models.CharField(max_length=100, null = False, blank=False)
    company_name = models.CharField(max_length=100, null = False, blank=False)
    id_no = models.CharField(max_length=100, null = False, blank=False)
    tel_number = models.CharField(null=False, max_length=100, blank=False)
    date = models. DateField(auto_now=True)
    temp = models.FloatField(null=False, default=False)
    def __str__(self):
        return self.name

class Temperature(models.Model):
    profile = models.ForeignKey(profiles,on_delete=models.CASCADE,null=True)
    temperature = models.FloatField(null=False)
    date = models. DateField(auto_now=True)
