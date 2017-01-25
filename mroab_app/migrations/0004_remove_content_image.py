# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mroab_app', '0003_content_slugger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image',
        ),
    ]
