# Generated by Django 4.1.7 on 2023-05-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
