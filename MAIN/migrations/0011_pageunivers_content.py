# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0010_auto_20151202_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageunivers',
            name='content',
            field=mezzanine.core.fields.RichTextField(default='add text here', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
