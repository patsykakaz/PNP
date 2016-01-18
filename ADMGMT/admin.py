#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *


publicite_extra_fieldsets = (
                (None,
                        {'fields': ('lien','media','formatPub')
                        }
                ),
        )

class PubliciteAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + publicite_extra_fieldsets


admin.site.register(Publicite, PubliciteAdmin)
