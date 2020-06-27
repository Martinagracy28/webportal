from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Alumini(models.Model):
    CHOICE =(('IT','Information Technology'),('CSE','Computer science Engineering'),('ECE','Electronic And Communication Engineering'),('EEE','Electrical And Electronic Engineering'),('MECH','Mechanical Engineering'))
    user = models.OneToOneField(User,null = True,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    collegename = models.TextField()
    department = models.CharField(max_length=200,choices=CHOICE)
    yearofpassing = models.DateField(default = timezone.now)
    companyname = models.TextField()
    currentposition = models.TextField()
    areaofdomain = models.TextField()
    email = models.EmailField()
    contactnumber = models.BigIntegerField()


    def __str__(self):
        return self.name

class Posts(models.Model):
    alumini = models.ForeignKey(Alumini,on_delete =models.SET_NULL,null = True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="pics",null = False)
    url = models.URLField()
    dateposted = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
