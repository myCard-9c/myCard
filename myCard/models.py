from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email, MaxValueValidator,URLValidator

class Card(models.Model):
    name = models.CharField(max_length=50,)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=100,blank = True)
    last_name = models.CharField(max_length=100,blank = True)
    email =  models.EmailField(max_length=150,blank = True)
    phone_no =  models.BigIntegerField(validators = [MaxValueValidator(9999999999)],default = 0000000000)
    location =  models.CharField(max_length=150,blank = True)
    occupation =  models.CharField(max_length=50,blank = True)
    website =  models.URLField(blank = True)
    picture = models.ImageField(blank = True)
    media_links =  models.URLField(blank = True)
    about =  models.CharField(blank = True,max_length=150)
    visibility =  models.BooleanField()
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
