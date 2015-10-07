# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0002_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='illustration',
            field=models.CharField(default=0, max_length=200, verbose_name='illustration'),
            preserve_default=False,
        ),
    ]
