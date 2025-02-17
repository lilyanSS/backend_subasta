# Generated by Django 2.2.16 on 2020-11-06 04:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_in_auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_price', models.FloatField(verbose_name='base_price')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('auction_date', models.DateField(null=True)),
                ('on_sale', models.BooleanField(default=True)),
                ('id_vehicle', models.IntegerField()),
            ],
        ),
    ]
