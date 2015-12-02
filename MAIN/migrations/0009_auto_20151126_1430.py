# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0008_auto_20151125_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicite',
            name='media',
            field=models.ImageField(null=True, upload_to='/home/patsykakaz/PNP/MAIN/static/media/publicite'),
        ),
        migrations.AlterField(
            model_name='siteextension',
            name='img_banner',
            field=models.ImageField(null=True, upload_to='/home/patsykakaz/PNP/MAIN/static/media/SITES/banner', blank=True),
        ),
        migrations.AlterField(
            model_name='siteextension',
            name='img_logo',
            field=models.ImageField(null=True, upload_to='/home/patsykakaz/PNP/MAIN/static/media/SITES/logo', blank=True),
        ),
    ]
