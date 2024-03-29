# Generated by Django 5.0.2 on 2024-02-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featuredcars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=20)),
                ('car_price', models.IntegerField()),
                ('car_image_url', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=4)),
                ('car_hp', models.CharField(max_length=8)),
                ('car_type', models.CharField(max_length=10)),
                ('car_odometer_reading', models.CharField(max_length=8)),
                ('car_description', models.TextField()),
            ],
        ),
    ]
