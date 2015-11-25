#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost


publicite_extra_fieldsets = (
                (None,
                        {'fields': ('lien','media','formatPub')
                        }
                ),
        )

class PubliciteAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + publicite_extra_fieldsets

class ArchiveAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "archive")
class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

SiteExtensionAdmin_extra_fieldsets = (
                (None,
                        {'fields': ('color','illustration','title_sub','baseline')
                        }
                ),
        )


class SiteExtensionAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + SiteExtensionAdmin_extra_fieldsets

admin.site.register(Publicite, PubliciteAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)
admin.site.register(SiteExtension, SiteExtensionAdmin)
