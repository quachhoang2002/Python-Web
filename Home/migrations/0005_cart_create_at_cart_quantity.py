# Generated by Django 4.0.4 on 2022-05-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='create_at',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=2120, max_length=50),
            preserve_default=False,
        ),
    ]
