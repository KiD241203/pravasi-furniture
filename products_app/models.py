from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=200)
    image = models.ImageField(upload_to='categories/')
    description = models.TextField(blank=True)
    
    class Meta:
        db_table = 'Category'
    
    def __str__(self):
        return self.name
    

class products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField( max_length=200)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    image = models.ImageField( upload_to='products/')
    description = models.TextField()
    available = models.BooleanField(default=True)
    
    
    class Meta:
        db_table = 'products'
    
    
    def __str__(self):
        return self.name
    