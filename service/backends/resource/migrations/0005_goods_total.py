# Generated by Django 2.1 on 2018-08-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0004_remove_goods_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='total',
            field=models.FloatField(default=0.0, verbose_name='商品总计'),
        ),
    ]