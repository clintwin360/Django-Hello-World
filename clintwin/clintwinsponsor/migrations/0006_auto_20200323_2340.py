# Generated by Django 3.0.4 on 2020-03-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clintwinsponsor', '0005_auto_20200323_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='dateDeregistered',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='dateRegistered',
            field=models.DateField(),
        ),
    ]
