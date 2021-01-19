# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet', models.CharField(max_length=400)),
                ('hashtag', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
