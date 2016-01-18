#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site

from mezzanine.blog.models import BlogCategory, BlogPost
from models import *


class AuthXMiddleware(object):
    def process_request(self,request):
        forbidden_domain = "lalettre"
        if forbidden_domain in request.META['HTTP_HOST'] and not request.user.is_authenticated() and not "admin" in request.path and not "login" in request.path:
            return HttpResponseRedirect('/user/login?next='+request.path)
        else: 
            print "request.META['HTTP_HOST'] = {}".format(request.META['HTTP_HOST'])
            print "request.user.is_authenticated = {}".format(request.user.is_authenticated())

class NavMiddleware(object):
    def process_template_response(self, request, response):
        all_sites = list(Site.objects.exclude(pk=3).order_by('domain'))
        all_sites.extend(list(Site.objects.filter(pk=3)))
        pages_univers = PageUnivers._base_manager.all()
        for page in pages_univers:
            print page.slug
        mainArticles = BlogPost._base_manager.filter(highlight=True).exclude(featured_image=None)[:2]
        # fetch color code 
        for article in mainArticles:
            try:
                article.extension_site = SiteExtension._base_manager.get(site=article.site)
            except:
                article.extension_site = False
        last_blogPosts = BlogPost._base_manager.exclude(highlight=True)
        # remove doubles
        last_blogPosts = last_blogPosts.distinct()
        last_blogPosts = last_blogPosts[0:18]
        # fetch color code
        for post in last_blogPosts:
            try:
                post.extension_site = SiteExtension._base_manager.get(site=post.site)
            except:
                post.extension_site = False

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

        response.context_data['mainSite'] = settings.MAIN_SITE
        response.context_data['all_sites'] = all_sites
        response.context_data['pages_univers'] = pages_univers
        response.context_data['last_blogPosts'] = last_blogPosts
        response.context_data['mainArticles'] = mainArticles[:3]
        return response

