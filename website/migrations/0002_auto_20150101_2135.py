# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='html',
            field=models.ManyToManyField(to='website.Code', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='rows',
            field=models.ManyToManyField(to='website.Row', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='row',
            name='columns',
            field=models.ManyToManyField(to='website.Column', null=True),
            preserve_default=True,
        ),
    ]
