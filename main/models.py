from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_image/')
    manufacturer = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    engine = models.PositiveIntegerField()
    engine_type = models.CharField(max_length=100)
    year = models.ImageField(max_length=100)
    amount_in_stock = models.IntegerField()
    sale = models.BooleanField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(max_length=200,default='',unique=True)

    def __str__(self):
        return self.name