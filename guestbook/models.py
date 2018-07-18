from django.db import models


class Guestbook(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    reg_date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return f'Guestbook({name}, {password}, {reg_date}, {content})'
