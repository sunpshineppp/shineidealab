# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='release_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('release_title', models.CharField(max_length=100)),
                ('release_content_brief', models.TextField(max_length=500)),
                ('release_photo_brief', models.URLField(blank=True)),
                ('release_content', models.TextField(max_length=50000)),
                ('release_photo', models.URLField(blank=True)),
                ('release_type', models.CharField(max_length=100)),
                ('release_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
