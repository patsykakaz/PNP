#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from models import *

from django.contrib.sites.models import Site
from mezzanine.blog.models import BlogCategory, BlogPost

class PubMiddleware(object):
    def process_template_response(self, request, response):
        try:
            habillage = Publicite._base_manager.get(formatPub='HABILLAGE')
            media = habillage.media.url.split('/')
            habillage.media = media[-1]
        except:
            habillage = False
        response.context_data['habillage'] = habillage
        try:
            squares = Publicite.objects.filter(formatPub='SQUARE')
            for square in squares :
                media = square.media.url.split('/')
                square.media = media[-1]
        except:
            squares = "empty"
        response.context_data['squares'] = squares
        return response


class NavMiddleware(object):
    def process_template_response(self, request, response):

        all_sites = Site.objects.exclude(name='default').order_by('id')
        pages_univers = PageUnivers._base_manager.all()
        mainArticles = BlogPost._base_manager.filter(highlight=True).exclude(featured_image=None)[:2]
        last_blogPosts = BlogPost._base_manager.exclude(highlight=True)[0:20]
        for post in last_blogPosts:
            try:
                post.extension_site = SiteExtension.objects.get(site=post.site)
            except:
                post.extension_site = False
        double = 0
        for X in mainArticles:
            if X in last_blogPosts:
                double += 1
        last_blogPosts = last_blogPosts[:20-double]

        for site in all_sites:
            site.all_cat = BlogCategory._base_manager.filter(site=site.id)
            site.highlights = BlogPost._base_manager.filter(site=site.id).exclude(featured_image='')[:3]
            try:
                siteExtension = SiteExtension._base_manager.filter(site=site.id).first()
                site.color = siteExtension.color
                site.css_class = siteExtension.css_class
                site.title_sub = siteExtension.title_sub
                site.baseline = siteExtension.baseline
                site.img_logo = siteExtension.img_logo.name.split('/')
                site.img_logo = site.img_logo[-1]
                site.img_banner = siteExtension.img_banner.name.split('/')
                site.img_banner = site.img_banner[-1]
            except:
                site.color = "#007099" 
                site.css_class = "default"
                site.title_sub = "---"
                site.baseline = "baseline is empty"
                site.img_logo = None
                site.img_banner = None

        response.context_data['all_sites'] = all_sites
        response.context_data['pages_univers'] = pages_univers
        response.context_data['last_blogPosts'] = last_blogPosts
        response.context_data['mainArticles'] = mainArticles[:3]
        return response
