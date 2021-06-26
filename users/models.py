from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import secrets

def passToken():
    while True:
        token = secrets.token_hex(40)
        if User.objects.filter(passtoken=token).count()==0:
            break
        return token


class Register(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = PhoneNumberField()
    email = models.EmailField()
    avatar = models.ImageField(default='default.jpg',upload_to='profile_pics')
    passtoken = models.CharField(max_length=40,default=passToken,unique=True)

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)

    

    