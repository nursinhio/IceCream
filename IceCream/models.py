from django.db import models

# Create your models here.
class IceCream(models.Model):
    name = models.CharField(max_length=20)
    taste = models.CharField(max_length=20)
    price = models.IntegerField()
