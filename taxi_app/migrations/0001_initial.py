# Generated by Django 5.1.6 on 2025-02-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_latitude', models.FloatField()),
                ('start_longitude', models.FloatField()),
                ('end_latitude', models.FloatField()),
                ('end_longitude', models.FloatField()),
                ('distance', models.FloatField()),
                ('fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
