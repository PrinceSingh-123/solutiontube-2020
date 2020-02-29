from django.db import models
from django.conf import settings

# Create your models here.
class Recharge(models.Model):
    code = models.IntegerField()
    # expiry_date = models.DateField(auto_now_add=False)


# class membership(models.Model):
#     user =  models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     active = models.BooleanField(default=False)

