# Generated by Django 4.2.4 on 2023-12-17 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0022_videogalerikategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGaleri01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('kapak_fotografi', models.URLField(blank=True, max_length=500, null=True)),
                ('url', models.URLField(max_length=500)),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('videogaleri_kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appname.videogalerikategori')),
            ],
        ),
    ]
