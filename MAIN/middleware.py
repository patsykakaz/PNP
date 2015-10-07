#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from models import *

from django.contrib.sites.models import Site
from mezzanine.blog.models import BlogCategory, BlogPost


class TEMPMiddleware(object):
    def process_template_response(self, request, response):
        all_sites = Site.objects.all().order_by('id')
        last_blogPosts = BlogPost._base_manager.exclude(featured_image=None)[2:14]
        for site in all_sites:
            site.all_cat = BlogCategory._base_manager.filter(site=site.id)
            site.highlights = BlogPost._base_manager.filter(site=site.id).exclude(featured_image='')[:3]
        mainArticles = BlogPost._base_manager.exclude(featured_image=None)[:2]
        response.context_data['all_sites'] = all_sites
        response.context_data['last_blogPosts'] = last_blogPosts
        response.context_data['mainArticles'] = mainArticles
        return response
