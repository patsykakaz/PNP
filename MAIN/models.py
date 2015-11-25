#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.sites.models import *
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from colorfield.fields import ColorField
from settings import MEDIA_ROOT

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
    #Overriding
    def save(self, *args, **kwargs):
        # in_menus empty pour exclure les archives des content_tree
        self.in_menus = []
        self.content = self.content.replace('src="','src="/static/archives/')
        # self.pdfContent = ''
        # inlines = PageRevue.objects.filter(revue=self)
        # for inline in inlines:
        #     inline.pdfContent = convert(str(inline.pdf.name))
        #     u = inline.pdfContent.decode('utf-8')
        #     self.pdfContent += u+'||'
        super(Archive, self).save(*args, **kwargs)

class SiteExtension(Page):
    color = ColorField(default='#007099')
    title_sub = models.CharField(max_length=128, null=True, blank=True)
    baseline = models.CharField(max_length=255, null=True, blank=True)

