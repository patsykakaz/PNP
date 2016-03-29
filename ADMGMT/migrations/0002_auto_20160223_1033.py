# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADMGMT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicite',
            name='formatPub',
            field=models.CharField(max_length=250, null=True, choices=[('HABILLAGE', 'HABILLAGE'), ('BANNER', 'BANNER')]),
        ),
        migrations.AlterField(
            model_name='publicite',
            name='media',
            field=models.ImageField(null=True, upload_to='/home/patsykakaz/PNP/MAIN/static/media/publicite'),
        ),
    ]
