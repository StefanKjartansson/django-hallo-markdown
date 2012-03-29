#!/usr/bin/env python
# -*- coding: utf-8
from django import forms
from django.conf import settings
from django.forms.util import flatatt
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


class HalloInput(forms.Textarea):

    def render(self, name, value, attrs=None):
        value = value or ''
        final_attrs = self.build_attrs(attrs, name=name)
        html = [u'<div class="hallo-block"><article class="edit"></article><textarea%s>%s</textarea></div>' % \
                (flatatt(final_attrs),
                 force_unicode(escape(value)))]
        return mark_safe(u'\n'.join(html))

    @property
    def media(self):
        return forms.Media(css= {'screen': [settings.STATIC_URL + "djhallo/hallo.css"]},
            js=(
                '//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js',
                '//ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js',
                settings.STATIC_URL + "djhallo/jquery-init.js",
                settings.STATIC_URL + "djhallo/showdown.js",
                settings.STATIC_URL + "djhallo/to-markdown.js",
                settings.STATIC_URL + "djhallo/hallo.js",
                settings.STATIC_URL + "djhallo/djhallo.js"))
