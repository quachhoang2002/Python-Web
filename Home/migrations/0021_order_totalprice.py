# Generated by Django 4.0.4 on 2022-05-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0020_orderdetail_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='TotalPrice',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]