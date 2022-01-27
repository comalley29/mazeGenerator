from django.db import models

# Create your models here.


class Style(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
