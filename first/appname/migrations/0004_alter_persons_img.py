# Generated by Django 4.2.4 on 2023-12-05 04:40

import appname.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0003_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='img',
            field=models.ImageField(default='defaultprofilephoto.jpg', upload_to=appname.models.personel_fotograf_path),
        ),
    ]
