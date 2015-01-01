# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150101_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='title',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='row',
            name='title',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
