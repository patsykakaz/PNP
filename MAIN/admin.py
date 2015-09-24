#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Archive

class ArchiveAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)

admin.site.register(Archive, ArchiveAdmin)