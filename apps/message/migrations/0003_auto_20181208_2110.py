# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-08 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20181208_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户留言信息', 'verbose_name_plural': '用户留言信息'},
        ),
        migrations.RenameField(
            model_name='usermessage',
            old_name='id',
            new_name='object_id',
        ),
    ]
