# Generated by Django 4.2.4 on 2023-12-13 11:00

import appname.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0016_mushafkategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mushaflar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('kapak_fotografi', models.ImageField(blank=True, null=True, upload_to=appname.models.kapakfoto_path_mushaflar)),
                ('pdf_dosya', models.FileField(blank=True, null=True, upload_to=appname.models.pdf_dosya_path_mushaflar)),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('mushaf_kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appname.mushafkategori')),
            ],
        ),
    ]