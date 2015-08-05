# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0002_auto_20150718_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='contact_mail',
            field=models.EmailField(verbose_name='MAIL', max_length=100),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='contact_message',
            field=models.TextField(verbose_name='留言', max_length=50000),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='contact_name',
            field=models.CharField(verbose_name='姓名', max_length=100),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='contact_type',
            field=models.CharField(verbose_name='問題種類', max_length=100),
        ),
    ]
