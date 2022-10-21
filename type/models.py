from django.db import models

from django.utils.text import slugify


class Type(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)        #slug of category
    name = models.CharField(max_length=30,unique=True)              #name of category

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def save(self,*args,**kwargs):
        self.slug =slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
