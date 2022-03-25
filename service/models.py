from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Xidmətlər(models.Model):
    icon = models.ImageField(upload_to="media/")
    basliq = models.TextField(max_length=50000)
    kicik_metn = models.TextField(max_length=50000)

    dahaetrafli_foto = models.ImageField(upload_to='825x400')
    vaxt = models.DateField()

    def __str__(self):
        return self.basliq

class Xidmətlər_ÜstMətn(models.Model):
    basliq = models.TextField(max_length=50000)
    metn = models.TextField(max_length=50000)

    def __str__(self):
        return self.basliq
