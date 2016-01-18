# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('MAIN', '0012_auto_20151210_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicite',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='Publicite',
        ),
    ]
