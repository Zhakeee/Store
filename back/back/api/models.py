from django.db import models

# Create your models here.

class Configurate(models.Model):
    chip = models.CharField(max_length=255)
    SSD = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    display = models.CharField(max_length=255)

class Products (models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    year = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    configure = models.JSONField()
    quantity = models.IntegerField()
    trash = models.BooleanField(default=False)
