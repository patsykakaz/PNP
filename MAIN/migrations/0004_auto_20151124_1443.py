# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0003_siteextension'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteextension',
            old_name='Title_sub',
            new_name='title_sub',
        ),
    ]
