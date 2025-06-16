from typing import Iterable
from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save()
    
    


class Product(models.Model):
    name = models.CharField(max_length=75)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        combined = f'{self.name}-{self.brand}'
        self.slug = slugify(combined)
        return super().save()
    
