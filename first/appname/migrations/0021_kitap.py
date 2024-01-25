# Generated by Django 4.2.4 on 2023-12-16 14:54

import appname.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0020_kitapkategori_mushaffarklari_pdf_dosya_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=200)),
                ('yazar', models.CharField(max_length=200)),
                ('yayin_tarihi', models.DateField()),
                ('sayfa_sayisi', models.IntegerField(default=0)),
                ('isbn', models.CharField(max_length=50)),
                ('kapak_fotografi', models.ImageField(blank=True, null=True, upload_to=appname.models.kapakfoto_path_kitaplar)),
                ('ozet', models.TextField()),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('kitap_kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appname.kitapkategori')),
            ],
        ),
    ]