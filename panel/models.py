from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=32)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return "用户"+self.username

