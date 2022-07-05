import email
from statistics import mode
from unicodedata import name
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=12, verbose_name='Имя')
    email = models.EmailField(verbose_name='Эл. почта')
    content_message = models.TextField(max_length=200, verbose_name='Письмо')
    date_message = models.DateTimeField(auto_now_add=True, verbose_name='Время получения')

    class Meta:
        ordering = ['-date_message']

    def __str__(self):
        return self.name