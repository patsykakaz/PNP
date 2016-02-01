#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from models import *

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
            banners = Publicite._base_manager.filter(formatPub='BANNER')[:3]
            for banner in banners :
                media = banner.media.url.split('/')
                banner.media = media[-1]
        except:
            banners = False
        response.context_data['banners'] = banners
        return response