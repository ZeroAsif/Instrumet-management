# Generated by Django 4.1.1 on 2023-05-15 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentapp', '0012_alter_bookinstrument_et_alter_bookinstrument_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstrument',
            name='et',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='bookinstrument',
            name='st',
            field=models.TimeField(),
        ),
    ]
