# -*- coding: utf-8 -*-
import logging
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('hostname', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
