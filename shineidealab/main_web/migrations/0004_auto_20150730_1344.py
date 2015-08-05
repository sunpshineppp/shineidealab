# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0003_auto_20150729_1827'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='release_data',
            new_name='ReleaseData',
        ),
    ]
