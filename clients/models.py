from django.db import models
from django.contrib.auth.models import User

app_label = "clients"
# Create your models here.
class Client(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    phone = models.CharField(max_length=13)
    gender = models.CharField(max_length=8)
    activation_code = models.CharField(max_length=8)

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id =models.ForeignKey(Client, on_delete=models.CASCADE, related_name="customer_id_address")
    detailed_address = models.CharField(max_length=128)
    region = models.CharField(max_length=64)
    province = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    barangay = models.CharField(max_length=128)
    address_status = models.BooleanField(default=False)
    phone = models.CharField(max_length=13)

class Region(models.Model):
    region_name = models.CharField(max_length=128)

class Province(models.Model):
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    province_name = models.CharField(max_length=128)
    province_code = models.CharField(max_length=6)

class City(models.Model):
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=3)

class Barangay(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    barangay_name = models.CharField(max_length=128)

