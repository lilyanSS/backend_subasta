# Generated by Django 2.2.16 on 2020-11-09 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]
