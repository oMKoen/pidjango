# Generated by Django 3.2.13 on 2022-06-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=30)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tod', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
