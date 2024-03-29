# Generated by Django 4.2.4 on 2023-12-12 06:41

import appname.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0011_temelkavramlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='YayinlarimizdanSecmeler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.TextField()),
                ('kapak_fotografi', models.ImageField(blank=True, null=True, upload_to=appname.models.kapakfoto_path_yayinlarimizdansecmeler)),
                ('pdf_dosya', models.FileField(blank=True, null=True, upload_to=appname.models.pdf_dosya_path_yayinlarimizdansecmeler)),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
            ],
        ),
    ]
