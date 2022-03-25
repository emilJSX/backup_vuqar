from distutils.command.upload import upload
from django.db import models

# Create your models here.

class SaytınBaşlığı(models.Model):
    title = models.CharField(max_length=50000)

class SaytinBaşlığıİcon(models.Model):
    icon = models.ImageField(upload_to="media/")

class Loqo(models.Model):
    loqo = models.ImageField(upload_to="media/")

class Giriş_Hissə(models.Model):
    foto = models.ImageField(upload_to="media/")
    metn = models.TextField(max_length=50000)

    def __str__(self):
        return self.metn

class Haqqımda(models.Model):
    foto = models.ImageField(upload_to="media/")
    basliq = models.TextField(max_length=50000)
    metn = models.TextField(max_length=50000)

    def __str__(self):
        return self.basliq

class AnaSəhifə_QəbulaYazıl_Mətnləri(models.Model):
    foto = models.ImageField(upload_to="media/")
    basliq = models.TextField(max_length=50000)
    metn = models.TextField(max_length=50000)

    def __str__(self):
        return self.basliq

class MüştəriRəyləri_ÜstMətn(models.Model):
    basliq = models.TextField(max_length=50000)
    metn = models.TextField(max_length=50000)

    def __str__(self):
        return self.basliq


class MüştəriRəyləri(models.Model):
    foto = models.ImageField(upload_to="media/")
    metn = models.TextField(max_length=50000)
    instagram = models.CharField(max_length=10000)

    def __str__(self):
        return self.metn

class Tez_Tez_VerilənSuallarÜstMətn(models.Model):
    basliq = models.TextField(max_length=50000)
    kicik_metn = models.TextField(max_length=50000)
    
    def __str__(self):
        return self.basliq

class Tez_Tez_VerilənSuallar(models.Model):
    foto = models.ImageField(upload_to="media/")
    sual_1 = models.TextField(max_length=50000)
    cavab_1 = models.TextField(max_length=50000)
    sual_2 = models.TextField(max_length=50000)
    cavab_2 = models.TextField(max_length=50000)
    sual_3 = models.TextField(max_length=50000)
    cavab_3 = models.TextField(max_length=50000)
    sual_4 = models.TextField(max_length=50000)
    cavab_4 = models.TextField(max_length=50000)
    sual_5 = models.TextField(max_length=50000)
    cavab_5 = models.TextField(max_length=50000)

class Footer(models.Model):
    metn = models.TextField(max_length=50000)

    def __str__(self):
        return self.metn

class MobileHaqqımızda(models.Model):
    foto = models.ImageField(upload_to='media/')