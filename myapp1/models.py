from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    surname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    surname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    data = models.DateField()
    data2 = models.DateField()
    place = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
