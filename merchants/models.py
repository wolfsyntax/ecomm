from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Merchant(models.Model):

    merchant_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=64)
    company_address = models.CharField(max_length=252)
    company_description = models.CharField(max_length=252)
    company_phone = models.CharField(max_length=16)
    coor_longitude = models.FloatField()
    coor_latitude = models.FloatField()

    def __str__(self):
        return self.company_name

