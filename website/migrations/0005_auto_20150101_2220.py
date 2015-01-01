# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150101_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='rel_row',
            field=models.ForeignKey(to='website.Row', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='row',
            name='rel_page',
            field=models.ForeignKey(to='website.Page', null=True),
            preserve_default=True,
        ),
    ]
