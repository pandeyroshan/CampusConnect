from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Notices(models.Model):
    Heading = models.CharField(max_length=500)
    Passage = models.TextField()
    Link = models.CharField(max_length=500,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Notice - "+str(self.id)
    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notice'

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Message from "+str(self.user)
    class Meta:
        verbose_name = 'Chat Data'
        verbose_name_plural = 'Chat Data'
