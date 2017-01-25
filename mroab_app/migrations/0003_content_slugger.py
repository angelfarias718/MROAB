# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mroab_app', '0002_auto_20170118_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='slugger',
            field=models.SlugField(default='timesquare', max_length=30),
            preserve_default=False,
        ),
    ]
