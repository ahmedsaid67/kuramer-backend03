# Generated by Django 4.2.4 on 2023-12-26 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0037_konferanslar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='konferanslar',
            old_name='egitmen',
            new_name='konusmaci',
        ),
        migrations.RemoveField(
            model_name='konferanslar',
            name='icerik',
        ),
    ]