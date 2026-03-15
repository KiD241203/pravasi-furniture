from django.db import models
from products_app.models import Category
# Create your models here.


class HeroCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    decription = models.TextField()
    image = models.ImageField( upload_to='hero/')
    
    class Meta:
        db_table = 'HeroCategory'
        
    def __str__(self):
        return  self.category.name
    
    