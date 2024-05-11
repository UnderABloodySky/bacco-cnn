from django.db import models

class MyModelPhoto(models.Model):
    photo = models.ImageField(upload_to='photos/')