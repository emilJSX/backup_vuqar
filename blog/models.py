from django.db import models
from django.views.generic import DetailView

# Create your models here.

class Bloq(models.Model):
    foto = models.ImageField(upload_to="media/")
    basliq = models.TextField(max_length=50000)
    metn = models.TextField(max_length=50000)
    vaxt = models.DateField()

    def __str__(self):
        return self.basliq
