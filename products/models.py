from django.db import models

# Create your models here.
from clients.models import *
from merchants.models import  *

class Category(models.Model):
    category_name = models.CharField(max_length=64)
    category_description = models.CharField(max_length=254)
    category_logo = models.CharField(max_length=254)
    category_status = models.CharField(max_length=12, default="1")


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    merchant_id = models.OneToOneField(Merchant,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=128)
    product_description = models.CharField(max_length=254)
    product_price = models.FloatField()
    brand = models.CharField(max_length=64)
    #variation_id = models.ForeignKey(Variation, on_delete=models.CASCADE)

    total_sold= models.IntegerField(default="0")
    discount_percentage = models.FloatField()
    total_rating = models.FloatField()

class Variation(models.Model):

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_name = models.CharField(max_length=32)

class Voucher(models.Model):
    product_id = models.OneToOneField(Product,on_delete=models.CASCADE)
    voucher_name = models.CharField(max_length=64)
    voucher_code = models.CharField(max_length=16)
    voucher_discount = models.IntegerField(default=0)


class ProductImage(models.Model):

    productImagePath = models.CharField(max_length=128)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Rating(models.Model):

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)