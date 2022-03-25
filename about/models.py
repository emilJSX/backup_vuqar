from django.db import models

# Create your models here.

class HaqqımızdaÜçSektoru(models.Model):
  foto_1 = models.ImageField(upload_to="media/")
  foto_2 = models.ImageField(upload_to="media/")
  foto_3 = models.ImageField(upload_to="media/")
