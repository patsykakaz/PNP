# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('MAIN', '0002_publicite'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteExtension',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('color', colorfield.fields.ColorField(default='#007099', max_length=10)),
                ('Title_sub', models.CharField(max_length=128, null=True, blank=True)),
                ('baseline', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
