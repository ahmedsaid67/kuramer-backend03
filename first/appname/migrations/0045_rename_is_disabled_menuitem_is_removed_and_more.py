# Generated by Django 4.2.4 on 2023-12-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0044_rename_baslik_puppup_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='is_disabled',
            new_name='is_removed',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='durum',
            field=models.BooleanField(default=True),
        ),
    ]