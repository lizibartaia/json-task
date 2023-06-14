from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50, default="")
    height = models.IntegerField()
    color = models.CharField(max_length=50)
    can_move = models.BooleanField(default=True)
    speed = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    


