# Generated by Django 3.0.6 on 2020-05-25 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200525_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(max_length=3, null=True),
        ),
    ]