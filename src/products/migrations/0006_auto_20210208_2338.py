# Generated by Django 3.1.6 on 2021-02-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210208_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
