# Generated by Django 3.2.13 on 2022-06-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pidjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='dataType',
            field=models.CharField(default='default', max_length=30),
        ),
    ]
