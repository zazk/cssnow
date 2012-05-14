# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.template import defaultfilters

from thumbs import ImageWithThumbsField

import Image
import os
import urlparse

# Create your models here.

class AuditableModel(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now=True)
    created_by = models.IntegerField('Creado por', editable=False, null=True, default=0)
    modified_by = models.IntegerField('Modificado por', editable=False, null=True, default=0)
    class Meta:
        abstract = True

class InfoSite(AuditableModel):
    email_contacto = models.EmailField(verbose_name=u'Email de Contacto')
    text_contacto = models.TextField(u'Escribenos', blank=True)
    text_telefono = models.TextField(u'Llamanos', blank=True)
    text_direccion = models.TextField(u'Encuentranos', blank=True)
    text_horarios = models.TextField(u'Horarios', blank=True)
    
    class Meta:
        ''' .'''
        verbose_name = u'Información del sitio'
        verbose_name_plural = u'Información del sitio'
        
    def __unicode__(self):
        return u'Información del Sitio'

#----------------------------
# BANNERS
#----------------------------
class Banner(AuditableModel):
    name = models.CharField("Nombre", max_length=120)
    descrip = models.TextField("Descripción", blank=True)
    desc = models.CharField("Enlace", max_length=220, blank=True)
    image = models.ImageField(verbose_name="Archivo", upload_to="banner/original")
    position = models.IntegerField("Orden", default=0) 

    class Meta:
        """ ."""
        verbose_name = u'Banner'
        verbose_name_plural = u'Banners'
        ordering = ['position']
        
    def __unicode__(self): 
        full = ' %s -> %s' % ( self.name , self.image)
        return full  

#----------------------------
# SECCIONES
#----------------------------
class Seccion(AuditableModel):
    name = models.CharField("Nombre", max_length=120)
    subtitulo = models.CharField("Subtitulo", max_length=120, blank=True)
    nick = models.CharField("Identificador", max_length=120, blank=True)
    url = models.CharField("Enlace", max_length=220, blank=True)
    descrip = models.TextField("Descripción", blank=True)
    position = models.IntegerField("Orden", default=0)
    banner = models.ManyToManyField(Banner,
                                        related_name='secciones',
                                        verbose_name=u"Banners",
                                        through='SeccionBanner')
    parent_category = models.ForeignKey("self",
                                        verbose_name=u"Seccion superior",
                                        blank=True,
                                        null=True)
    
    class Meta:
        """ ."""
        verbose_name = u'Seccion'
        verbose_name_plural = u'Secciones'
        ordering = ['position'] 
        
    def __unicode__(self):
        full = ' %s' % ( self.name )
        return full

#----------------------------
# BANNERS DE SECCIONES
#----------------------------
class SeccionBanner(models.Model):
    banner = models.ForeignKey(Banner)
    seccion = models.ForeignKey(Seccion)
    position = models.IntegerField("Orden",default=0)

    class Meta:
        verbose_name= u'Banner de Seccion'
        verbose_name_plural = u'Banners de Seccion'
        ordering = ['position']
 