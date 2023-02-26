from django.db import models
class Friend(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
