# Generated by Django 3.0.4 on 2020-03-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clintwinsponsor', '0004_auto_20200323_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='dateDeregistered',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dateRegistered',
            field=models.DateField(),
        ),
    ]