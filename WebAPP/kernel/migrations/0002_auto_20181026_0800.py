# Generated by Django 2.1.2 on 2018-10-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='lng',
            field=models.FloatField(),
        ),
    ]
