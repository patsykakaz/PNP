# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0003_archive_illustration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='illustration',
            field=models.CharField(max_length=200, null=True, verbose_name='illustration', blank=True),
        ),
    ]
