# Generated by Django 3.2.13 on 2022-10-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0005_shelly2_5_rollervalues_shelly2_5config_shelly2_5relay_config_shelly2_5relayvalues_shelly2_5values_sh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shellyconfig',
            name='mqqt_id',
            field=models.CharField(max_length=100),
        ),
    ]