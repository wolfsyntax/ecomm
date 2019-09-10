from django.shortcuts import render

# Create your views here.
from products.models import *
from merchants.models import Merchant
from clients.models import Customer

PACKAGE_SIZE = (
    ('XS', 'Extra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large')
)

PAY_OPTION = (
    ('Cash on Delivery', 'Cash on Delivery'),
    ('Wallet', 'Wallet'),
    ('Bank Transfer', 'Bank Transfer')
)


#class OrderDetail(models.Model):

#    product_id = models.ForeignKey(Product, on_delete= models.CASCADE)
#    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
#    voucher_id = models.ForeignKey(Voucher, on_delete=models.CASCADE, null=True)
#    package_size = models.CharField(choices=PACKAGE_SIZE)
#    tracking_code =models.CharField(max_length=32)
#    quantity

#class Order(models.Model):

#    orderDetail_id =
