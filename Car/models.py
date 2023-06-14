from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    speed = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.brand + self.model
