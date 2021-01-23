from django.db import models

# Create your models here.

class dars(models.Model):
    img = models.ImageField(upload_to='dars_rasmlari')
    ism = models.CharField(max_length=30)
    fan = models.CharField(max_length=30)
    dic = models.TextField(max_length=80)



class tadbirlar(models.Model):
    img = models.ImageField(upload_to='tadbir_rasmlari')
    kun = models.CharField(max_length=2)
    oy = models.CharField(max_length=3)
    yil = models.CharField(max_length=4)
    nomi = models.CharField(max_length=25)
    malumot = models.TextField(max_length=100)


class oqituvchilar(models.Model):
    rasmi = models.ImageField(upload_to='o`qituvchilar_rasmi')
    ism_familyasi = models.CharField(max_length=35)
    lavozimi = models.CharField(max_length=35)
    malomut = models.CharField(max_length=35)



class photolar(models.Model):
    rasm = models.ImageField(upload_to='rasmlari')

class kitob(models.Model):
    kitob_nomi = models.CharField(max_length=50)
    malumot = models.TextField()
    kiritish = models.FileField(upload_to='kitoblar')