# -*- coding: utf-8 -*-
""" Admin website. """

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from local_apps.website.models import Banner, InfoSite, Seccion 

class InfoSiteAdmin(admin.ModelAdmin):
    model = InfoSite
    class Media:
        js = ('/static/nicEdit/nicEdit.js', '/static/nicEdit/nicEdit_conf.js')

class SeccionBanner(admin.TabularInline):
    model = Seccion.banner.through
    sortable_field_name = 'position'
    extra = 0

class SeccionInline(admin.TabularInline):
    model = Seccion
    sortable_field_name = 'position'
    exclude = ('descrip', 'subtitulo', 'url',)
    extra = 0

class SeccionAdmin(admin.ModelAdmin):
    model = Seccion  
    inlines = [SeccionInline,SeccionBanner]
    list_display = ['name', 'parent_category']

    class Media:
        js = ('/static/nicEdit/nicEdit.js', '/static/nicEdit/nicEdit_conf.js')

class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['name', 'image']
    exclude = ('descrip', 'desc',)


admin.site.register(InfoSite, InfoSiteAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Banner, BannerAdmin) 