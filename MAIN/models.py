#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import *

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.utils.sites import current_site_id, current_request
from colorfield.fields import ColorField

class Publicite(Page):
    lien = models.CharField(max_length=255, null=True, blank=True)
    media = models.ImageField(upload_to=MEDIA_ROOT+'/publicite', null=True)
    OPTION_FORMAT_PUB = (
        ('HABILLAGE','HABILLAGE'),
        ('SQUARE', 'SQUARE'),
        ('COLONNE','COLONNE'),
    )
    formatPub = models.CharField(choices=OPTION_FORMAT_PUB, max_length=250, null=True)

class Client(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=128)
    is_active = True
    is_staff= False

class Archive(Page, RichText):
    illustration = models.CharField(max_length=200,verbose_name='illustration',null=True,blank=True)

    def save(self, *args, **kwargs):
        # in_menus empty pour exclure les archives des content_tree
        self.in_menus = []
        self.content = self.content.replace('src="','src="/static/archives/')
        super(Archive, self).save(*args, **kwargs)

class SiteExtension(Page):
    color = ColorField(default='#007099')
    img_logo = models.ImageField(upload_to=MEDIA_ROOT+'/SITES/logo', null=True, blank=True, verbose_name='logo')
    img_banner = models.ImageField(upload_to=MEDIA_ROOT+'/SITES/banner', null=True, blank=True, verbose_name='banner', help_text='bannière pour la page d\'acceuil du sous-site')
    css_class = models.CharField(max_length=100, null=True, blank=True)
    title_sub = models.CharField(max_length=128, null=True, blank=True)
    baseline = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.in_menus = []
        self.css_class = "ID_"+str(current_site_id())+self.color.replace('#','_')
        super(SiteExtension, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'EXTENSION_SITE'

class PageUnivers(Page, RichText):
    illustration = models.ImageField(upload_to=MEDIA_ROOT+'/SITES/universPNP', null=True, blank=True, verbose_name='illustration')

    class Meta:
        verbose_name = 'UNIVERS_PNP'


