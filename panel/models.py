from django.contrib.auth.models import User
from django.db import models


class Friend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    latitude = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    longitude = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return "用户" + self.user.get_username()
