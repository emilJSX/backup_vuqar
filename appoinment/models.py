from django.db import models

# Create your models here.

class Form_Foto(models.Model):
    foto = models.ImageField(upload_to="media/")