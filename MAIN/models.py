#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText

class Client(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=128)
    is_active = True
    is_staff= True

class Archive(Page, RichText):
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