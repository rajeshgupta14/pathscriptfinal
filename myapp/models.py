from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
#from myapp.models import Product
   
class Client(models.Model):
     id=models.CharField(max_length=30, primary_key=True)
     clientname=models.CharField(max_length=30)
     userid=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)
     
     
     
     def __str__(self):
        return self.clientname
     
class User(AbstractUser):
     
     clientid = models.ForeignKey(Client, null=True, blank=True)
     location = models.CharField(max_length=30, blank=True)
     
class Product(models.Model):
    
    name=models.CharField(max_length=40,blank=True,null=True)
    description=models.TextField(max_length=500,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    
    name=models.CharField(max_length=30,blank=True,null=True)
    client=models.ForeignKey(Client,blank=True,null=True)
    product=models.ForeignKey(Product,blank=True,null=True)
    user=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)
    
    def __str__(self):
        return self.name
    
