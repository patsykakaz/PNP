from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from mezzanine.pages.page_processors import processor_for
from mezzanine.blog.models import BlogPost, BlogCategory
from .models import *

from mezzanine.core.request import current_request

# @processor_for('/')
# def processor_home(request,page):
    # request = current_request()
    # print request.get_host().lower()
    # return locals()

@processor_for(PageUnivers)
def processor_revue(request, page):
    PageUniv = PageUnivers.objects.filter(title=page.title)
    PageUniv = PageUniv[0]
    try:
        couv = PageUniv.illustration.url.split('/')
        PageUniv.couverture = couv[-1]
    except:
        couv = False
    return locals()
