# -*- coding: utf-8 -*-
from django import forms


text = {'class': 'text'}
text_required = {'class': 'text', 'required': 'required'}


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre')
    name.widget.attrs.update(text_required)
    last = forms.CharField(label='Apellido')
    last.widget.attrs.update(text_required)
    email = forms.EmailField(label='Email')
    email.widget.attrs.update(text_required)
    telefono = forms.CharField(required=False)
    telefono.widget.attrs.update(text)
    message = forms.CharField(label='Mensaje',widget=forms.Textarea)
    message.widget.attrs.update({'required': 'required'})