# Generated by Django 4.2.4 on 2023-12-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0030_fotogaleri_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='durum',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='image',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
    ]