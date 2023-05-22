# Generated by Django 4.1.7 on 2023-05-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('eng', 'English'), ('mal', 'Malayalam'), ('ara', 'Arabic')], max_length=3)),
                ('author', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
