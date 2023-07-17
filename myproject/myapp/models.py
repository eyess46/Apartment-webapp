from django.db import models
from datetime import datetime

# Create your models here.


class Properties(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    location = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    area_lenght = models.CharField(max_length=500)
    beds = models.CharField(max_length=500)
    baths = models.CharField(max_length=500)
    garage = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')




class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Properties = models.ForeignKey(Properties, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)



class Top(models.Model):
    address = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')




class Seravice(models.Model):
    name = models.CharField(max_length=5000000)
    details = models.CharField(max_length=1000)



    
class News(models.Model):
    details = models.CharField(max_length=5000000)
    property_type = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=datetime.now, blank=True)

     

    
class Contactform(models.Model):
    name = models.CharField(max_length= 100)
    subject = models.CharField(max_length= 100)
    email = models.EmailField(unique= True)
    message = models.CharField(max_length= 900)
    image = models.ImageField(upload_to= "images/")