# Generated by Django 4.1.1 on 2023-05-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentapp', '0011_alter_bookinstrument_aprove_delete_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstrument',
            name='et',
            field=models.TimeField(unique=True),
        ),
        migrations.AlterField(
            model_name='bookinstrument',
            name='st',
            field=models.TimeField(unique=True),
        ),
    ]
