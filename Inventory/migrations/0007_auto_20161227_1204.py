# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_purchase_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='items',
            new_name='stock',
        ),
    ]