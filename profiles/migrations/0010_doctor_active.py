# Generated by Django 3.0.6 on 2020-05-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20200525_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
