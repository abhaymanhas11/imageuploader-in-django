from django.db import models

# Create your models here.
class imageuploader(models.Model):
    image=models.ImageField(upload_to='images')