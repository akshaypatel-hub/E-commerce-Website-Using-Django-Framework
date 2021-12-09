from django.db import models

# Create your models here.

# Product Login

class Productlogin(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    question =models.CharField(max_length=200)

    def __str__(self):
        return self.username

# Product

class Product(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_price =models.FloatField()
    Product_description = models.CharField(max_length=200)
    Product_image = models.ImageField(upload_to='product_img',blank=True)

    def __str__(self):
        return self.Product_name

# Cart

class Cart(models.Model):
    Prod_name = models.CharField(max_length=200)
    Prod_price = models.FloatField()
    Prod_desci = models.CharField(max_length=200)
    Prod_image = models.CharField(max_length=250)

    def __str__(self):
        return self.Prod_name



