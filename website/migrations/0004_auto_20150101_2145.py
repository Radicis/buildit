# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150101_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='title',
        ),
        migrations.RemoveField(
            model_name='row',
            name='title',
        ),
    ]
