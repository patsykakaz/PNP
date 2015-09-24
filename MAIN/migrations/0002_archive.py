# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('MAIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
    ]
