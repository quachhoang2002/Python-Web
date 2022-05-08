# Generated by Django 4.0.4 on 2022-05-08 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_orderdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.cart'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]