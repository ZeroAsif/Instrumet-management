# Generated by Django 4.1.1 on 2023-05-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrumentapp', '0010_bookinstrument_aprove_alter_approve_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstrument',
            name='Aprove',
            field=models.BooleanField(default=False, verbose_name='Aprove'),
        ),
        migrations.DeleteModel(
            name='Approve',
        ),
    ]
