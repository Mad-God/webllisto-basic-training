# Generated by Django 3.1.4 on 2022-04-29 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='code',
        ),
    ]
