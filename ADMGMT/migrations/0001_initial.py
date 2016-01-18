# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('lien', models.CharField(max_length=255, null=True, blank=True)),
                ('media', models.ImageField(null=True, upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/publicite')),
                ('formatPub', models.CharField(max_length=250, null=True, choices=[('HABILLAGE', 'HABILLAGE'), ('SQUARE', 'SQUARE'), ('COLONNE', 'COLONNE')])),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
