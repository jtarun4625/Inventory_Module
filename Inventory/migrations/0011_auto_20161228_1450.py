# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0010_auto_20161228_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='purchase',
            field=models.ManyToManyField(related_name='purchase', to='Inventory.Purchase'),
        ),
    ]