from django.db import models

# Create your models here.

class City(models.Model):            #slug of city
    name = models.CharField(max_length=50,unique=True)
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        
    def __str__(self):
        return self.name


