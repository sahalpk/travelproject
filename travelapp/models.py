from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics1')
    desc=models.TextField()


    def __str__(self) :
        return self.name #ithe admin ile upload cheytha file nte pere kanikn eyne ithe cheythlele object akie kanikum verthe cheyane anne