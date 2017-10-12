from django.db import models


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    picture=models.TextField()


class People2(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    picture = models.TextField()

class People3(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    picture = models.TextField()

class People4(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    picture = models.TextField()