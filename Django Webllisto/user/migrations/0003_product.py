# Generated by Django 3.1.4 on 2022-04-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_custom_mig_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(blank=True, choices=[('Supplier1', 'sup1'), ('Supplier2', 'sup2'), ('Supplier3', 'sup3'), ('Supplier4', 'sup4'), ('Supplier5', 'sup5')], max_length=100, null=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('code', models.IntegerField(blank=True, default=-1, null=True)),
                ('index', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
