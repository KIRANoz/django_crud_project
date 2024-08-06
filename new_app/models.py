from django.db import models

# Create your models here.
class Furniture(models.Model):
    furniture_types = (
        ('plastic','plastic'),
        ('steel','steel'),
        ('wooden','wooden')
    )
    Name = models.CharField(max_length=25)
    Price = models.IntegerField()
    Types = models.CharField(max_length=17, choices=furniture_types)
    Details = models.TextField()
