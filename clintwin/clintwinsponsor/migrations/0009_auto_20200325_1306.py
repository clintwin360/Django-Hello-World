# Generated by Django 3.0.4 on 2020-03-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clintwinsponsor', '0008_auto_20200325_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicaltrial',
            name='exclusionCriteria',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clinicaltrial',
            name='inclusionCriteria',
            field=models.CharField(max_length=100),
        ),
    ]
