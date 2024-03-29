from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f'User({email}, {password}, {name}, {gender})'
