from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator,\
    RegexValidator


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")]  ,max_length=20, null = True , blank=True)
    dob = models.DateField(null=True , blank=True)
    profileimg=models.ImageField(upload_to = "profileimg", null=True , blank=True)

    def __str__(self):
        return  f"{self.user}"