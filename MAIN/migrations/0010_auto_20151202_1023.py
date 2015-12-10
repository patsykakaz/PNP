# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('MAIN', '0009_auto_20151126_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageUnivers',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('illustration', models.ImageField(upload_to='/home/patsykakaz/PNP/MAIN/static/media/SITES/universPNP', null=True, verbose_name='logo', blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'UNIVERS_PNP',
            },
            bases=('pages.page',),
        ),
        migrations.AlterModelOptions(
            name='siteextension',
            options={'ordering': ('_order',), 'verbose_name': 'EXTENSION_SITE'},
        ),
        migrations.AlterField(
            model_name='siteextension',
            name='img_banner',
            field=models.ImageField(help_text="banni\xe8re pour la page d'acceuil du sous-site", upload_to='/home/patsykakaz/PNP/MAIN/static/media/SITES/banner', null=True, verbose_name='banner', blank=True),
        ),
        migrations.AlterField(
            model_name='siteextension',
            name='img_logo',
            field=models.ImageField(upload_to='/home/patsykakaz/PNP/MAIN/static/media/SITES/logo', null=True, verbose_name='logo', blank=True),
        ),
    ]
