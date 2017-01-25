# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
