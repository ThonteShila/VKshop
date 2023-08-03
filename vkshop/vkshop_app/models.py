from django.db import models
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,null=True,blank=True)                              #slug-in http ling we can give valid name
    category_image=models.ImageField(upload_to="categories")

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    price=models.IntegerField()
    product_description=models.TextField()

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image")
    image=models.ImageField(upload_to="product")