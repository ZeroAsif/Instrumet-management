from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class AddInsrument(models.Model):
    instrument_name = models.CharField(max_length=100)
    instrument_desc = models.TextField()
    instrument_img = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


# class Approve(models.Model):
#     approve = models.BooleanField('Approve', default=False)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
   
class BookInstrument(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    your_name = models.CharField(max_length=100)
    iname = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    st = models.TimeField()
    et = models.TimeField()
    Aprove = models.BooleanField('Aprove', default=False)

    def __str__(self) -> str:
        return self.iname + " >>>>>>> " + self.your_name