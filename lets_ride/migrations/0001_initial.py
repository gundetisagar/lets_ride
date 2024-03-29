# Generated by Django 2.2.1 on 2020-07-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('from_place', models.CharField(max_length=50)),
                ('to_place', models.CharField(max_length=50)),
                ('flexible_timings', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(null=True)),
                ('start_date_time', models.DateTimeField(null=True)),
                ('end_date_time', models.DateTimeField(null=True)),
                ('no_of_seats', models.IntegerField()),
                ('luggage_quantity', models.IntegerField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
