from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    
    # Accounts
    url(r'^accounts/', include('external_apps.registration.backends.default.urls')),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # Front-end 
    # url(r'^(?P<slug>[-\w]+)/$', 'local_apps.website.views.home', name='home'),
    url(r'^$', 'local_apps.website.views.home', name='home'),
    url(r'^fotos/$', 'local_apps.website.views.foto', name='foto'),
    url(r'^video/(?P<id>\d*)/$', 'local_apps.website.views.ver_video', name='ver-video'),
    url(r'^videos/$', 'local_apps.website.views.video', name='video'),
    url(r'^articulos/$', 'local_apps.website.views.articulo', name='articulo'),
    url(r'^nuestro-consultorio/$', 'local_apps.website.views.nuestro_consultorio', name='nuestro-consultorio'),
    url(r'^envianos-tus-dudas/$', 'local_apps.website.views.envianos_dudas', name='envianos-dudas'),
    url(r'^servicio/(?P<id>\d*)/$', 'local_apps.website.views.servicio', name='servicio'),
)