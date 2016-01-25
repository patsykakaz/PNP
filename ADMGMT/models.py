#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.sites.models import *
from mezzanine.pages.models import Page

class Publicite(Page):
    lien = models.CharField(max_length=255, null=True, blank=True)
    media = models.ImageField(upload_to=settings.MEDIA_ROOT+'/publicite', null=True)
    OPTION_FORMAT_PUB = (
        ('HABILLAGE','HABILLAGE'),
        ('BANNER', 'BANNER'),
    )
    formatPub = models.CharField(choices=OPTION_FORMAT_PUB, max_length=250, null=True)

    def save(self, *args, **kwargs):
        # in_menus empty -> exclude from content_trees
        self.in_menus = []
        super(Publicite, self).save(*args, **kwargs)