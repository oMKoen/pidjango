# Generated by Django 3.2.13 on 2022-07-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='svalue',
            field=models.CharField(default='default', max_length=30),
        ),
    ]
