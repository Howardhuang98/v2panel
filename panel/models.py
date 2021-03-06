from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from markdownx.models import MarkdownxField


class Friend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    latitude = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    longitude = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    invite_code = models.CharField(max_length=12, blank=True)
    who_invite = models.ForeignKey(to='self', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "用户" + self.user.get_username()


# 信号函数，当User创建新实例的时候，Friend也跟着创建
@receiver(post_save, sender=User)
def handler_user_friend(sender, instance, created, **kwargs):
    if created:
        Friend.objects.create(user=instance)
    else:
        instance.friend.save()


class Markdown(models.Model):
    name = models.CharField(max_length=10)
    content = MarkdownxField()
