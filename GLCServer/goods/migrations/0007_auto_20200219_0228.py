# Generated by Django 2.2.6 on 2020-02-19 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20200219_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 2, 28, 11, 440794), verbose_name='教材过期时间(默认在创建教材后的三个月过期)'),
        ),
    ]