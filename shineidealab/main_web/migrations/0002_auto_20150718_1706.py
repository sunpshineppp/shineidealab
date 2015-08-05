# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_mail', models.EmailField(max_length=100)),
                ('contact_type', models.CharField(max_length=100)),
                ('contact_message', models.TextField(max_length=50000)),
                ('contact_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='release_data',
            name='release_photo',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='release_data',
            name='release_photo_brief',
            field=models.URLField(max_length=500),
        ),
    ]
