from django.db import models
from django.urls import reverse


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    picture=models.TextField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})


class People2(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    picture = models.TextField()
    def get_absolute_url(self):
        return reverse('detail2',kwargs={'pk':self.pk})

class People3(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    picture = models.TextField()
    def get_absolute_url(self):
        return reverse('detail3',kwargs={'pk':self.pk})

class People4(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    picture = models.TextField()
    def get_absolute_url(self):
        return reverse('detail4',kwargs={'pk':self.pk})