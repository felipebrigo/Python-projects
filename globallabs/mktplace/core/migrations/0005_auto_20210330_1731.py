# Generated by Django 3.1.2 on 2021-03-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210323_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='maxVol',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contract',
            name='minVol',
            field=models.IntegerField(default=0),
        ),
    ]