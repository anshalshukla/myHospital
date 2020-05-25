# Generated by Django 3.0.6 on 2020-05-24 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20180322_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='closed_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='filed_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]