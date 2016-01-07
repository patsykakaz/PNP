#-*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'login/$', 'USERMGMT.views.connect', name='connect'),
    url(r'logout/$', 'USERMGMT.views.killUser', name='killUser'),
    url(r'display/$', 'USERMGMT.views.showUser', name='showUser'),
    url(r'modification/$', 'USERMGMT.views.changeUser', name='changeUser'),
    url(r'test_log_req/$', 'USERMGMT.views.test_log_req', name='test_log_req'),
    # url(r'register/$', 'USERMGMT.views.register', name='register'),
)
