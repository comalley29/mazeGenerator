from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Style(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name

class Maze(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(150)])
    height = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(150)])
