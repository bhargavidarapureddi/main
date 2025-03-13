from django.db import models

# Create your models here.
class Product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    price=models.FloatField()