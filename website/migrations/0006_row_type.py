# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150101_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='row',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
