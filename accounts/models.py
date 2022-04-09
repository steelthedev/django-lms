from distutils.command.upload import upload
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Sum

from django.shortcuts import reverse

# Create your models here.
#class Customer(models.Model):
  #User=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
  #name=models.CharField(max_length=200,null=True)
  #Email=models.EmailField(max_length=200)
  
  #def __str__(self):
   # return self.name
   

class Profile(models.Model):


    INSTRUCTOR ='instructor'
    STUDENT = 'student'
    ADMIN = 'admin'

    STATUS_CHOICES =[
        (INSTRUCTOR, 'Instructor'),
        (STUDENT, 'Student'),
        (ADMIN,'Admin')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='user/',blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True)
    status = models.CharField(max_length=20 ,choices=STATUS_CHOICES, blank=True)
    username = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    about_me = models.TextField(blank=True)


    def __str__(self):
        return self.user.username


    def get_profile_picture(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance= None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



