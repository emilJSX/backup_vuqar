from django.db import models

# Create your models here.

class Telefon_Email_Mekan(models.Model):
    email = models.CharField(max_length=50000)
    mekan = models.TextField(max_length=50000)

class Form_Şəkil(models.Model):
    foto = models.ImageField(upload_to="media/")

class Sosial_Şəbəkələr(models.Model):
    facebook = models.TextField(max_length=50000)
    youtube = models.TextField(max_length=50000)
    instagram = models.TextField(max_length=50000)