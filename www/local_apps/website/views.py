# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response as render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponseRedirect

from local_apps.website.models import Banner, InfoSite, Seccion 
from local_apps.website.forms import ContactForm


def home(request):
    return render('website/home.html', locals(),
        context_instance=RequestContext(request))
  
def envianos_dudas(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            htmly = get_template('website/email-contacto.html')
            name = form.cleaned_data['name']
            last = form.cleaned_data['last']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            message = form.cleaned_data['message']

            d = Context({ 'name':name, 'last':last, 'email':email, 'message':message })
            html_content = htmly.render(d)
            subject = u"Contacto - %s" % (name)
            
            msg = EmailMessage(subject,  html_content, email,
                    [InfoSite.objects.latest('id').email_contacto],['juandedioz@gmail.com',email],
                    headers = {'Reply-To': email})
            msg.content_subtype = "html"
            msg.send()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render('website/contact-thanks.html', locals(),
        context_instance=RequestContext(request))
 