# Generated by Django 3.0.10 on 2020-09-08 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200908_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]