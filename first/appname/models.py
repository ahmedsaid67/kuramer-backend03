import os
from django.db import models
from datetime import datetime



def get_image_path(instance, filename):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return os.path.join('sliders/', f'{timestamp}_{filename}')


class Slider(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Menu (models.Model):
    title = models.CharField(max_length=255)
    selected = models.BooleanField(default=False)

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255,blank=True,null=True)
    order = models.PositiveIntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    is_disabled = models.BooleanField(default=False)



class PersonelTuru(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


import uuid


def personel_fotograf_path(instance, filename):
    # Dosya uzantısını al (örn: .jpg, .png)
    ext = filename.split('.')[-1]
    # Benzersiz bir dosya ismi oluştur
    filename = f"{uuid.uuid4()}.{ext}"
    # 'media/personel/' altında bu dosyayı sakla
    return f'personel/{filename}'


class Persons(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    unvan= models.CharField(max_length=100,null=True, blank=True)
    personel_turu = models.ForeignKey(PersonelTuru, on_delete=models.CASCADE,null=True, blank=True)
    img = models.ImageField(upload_to=personel_fotograf_path, default='defaults/defaultprofilephoto.jpeg')
    durum = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ad} {self.soyad}"




