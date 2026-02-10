from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class abstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
class Category(abstractBaseModel):
    name = models.CharField(max_length=255)

    class Meta: 
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Item(abstractBaseModel):
    category = models.ForeignKey(Category,related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, blank=True, null=True,related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name