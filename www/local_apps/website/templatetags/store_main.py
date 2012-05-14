# -*- coding: utf-8 -*- 

from django.shortcuts import get_object_or_404
from django import template
from local_apps.website.models import Banner, InfoSite, Seccion  
from django.db import connection
from settings import STATIC_URL

register = template.Library()

@register.inclusion_tag('website/header.html')
def header():

    return locals()
 
