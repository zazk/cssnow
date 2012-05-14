# -*- coding: utf-8 -*-
from django import forms


text = {'class': 'text'}
text_required = {'class': 'text', 'required': 'required'}


class ContactForm(forms.Form):
    name = forms.CharField()
    name.widget.attrs.update(text_required)
    last = forms.CharField()
    last.widget.attrs.update(text_required)
    email = forms.EmailField()
    email.widget.attrs.update(text_required)
    telefono = forms.CharField(required=False)
    telefono.widget.attrs.update(text)
    message = forms.CharField(widget=forms.Textarea)
    message.widget.attrs.update({'required': 'required'})