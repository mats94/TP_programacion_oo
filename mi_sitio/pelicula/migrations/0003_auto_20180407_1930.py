# Generated by Django 2.0.3 on 2018-04-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0002_auto_20180321_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]