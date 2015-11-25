# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0004_auto_20151124_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteextension',
            name='css_class',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteextension',
            name='illustration',
            field=models.ImageField(null=True, upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/SITES'),
        ),
        migrations.AlterField(
            model_name='publicite',
            name='media',
            field=models.ImageField(null=True, upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/publicite'),
        ),
    ]
