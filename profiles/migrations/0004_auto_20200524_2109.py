# Generated by Django 3.0.6 on 2020-05-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200524_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='contact_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
