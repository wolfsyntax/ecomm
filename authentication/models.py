from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):

    customer_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    phone = models.CharField(max_length=13, error_messages={}, help_text="")

    gender = models.CharField(max_length=6, choices=(
        ("male", "Male"),
        ("female", "Female"),
    ), error_messages={'required': 'Gender is required.'})

    def __str__(self):
        return 'Profile for user {}'.format(self.user)

    class Meta:
    	db_table='tbl_profile'
