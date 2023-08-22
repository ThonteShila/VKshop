from django.db import models
# Create your models here.

class Owner_details(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    owner_email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    last_update_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    is_owner=models.BooleanField(default=False)
    comp_address=models.CharField(max_length=200)
    comp_name=models.CharField(max_length=100)


class Product_details(models.Model):
    product_name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_name=models.CharField(max_length=200)
    category_slug=models.SlugField(unique=True,null=True,blank=True)                              #slug-in http ling we can give valid name
    category_image=models.ImageField(upload_to="categories")
    price=models.IntegerField()
    product_description=models.TextField()
    product_image=models.ImageField(upload_to="product")