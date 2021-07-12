from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(to=User, on_delete=CASCADE,null=True, blank=True)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    last_edit = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 100 , default='publish',  choices=(('publish','publish'), ('draft','draft')))
    img=models.ImageField(upload_to = "blogs", null=True)
    
    def __str__(self):
        return  f"{self.title}"


class Contact(models.Model):
    Email=models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return f"{self.Email}"