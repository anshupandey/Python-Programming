from django.db import models

# Create your models here.

class products(models.Model):
    productname = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")