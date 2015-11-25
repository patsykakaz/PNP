# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0006_auto_20151125_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteextension',
            name='css_class',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
