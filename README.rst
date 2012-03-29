=====================
Django Hallo Markdown
=====================

A `hallo`_ js markdown editor wrapper for Django. Made for use in FeinCMS,
supports multiple editors on the same page.


.. _`hallo`: http://bergie.github.com/hallo/markdown.html

Installation
============

You can install django-hallo-markdown either via the Python Package Index (PyPI)
or from source.

To install using `pip`,::

    $ pip install -U django-hallo-markdown

To install using `easy_install`,::

    $ easy_install -U django-hallo-markdown


Example Usage with FeinCMS
==========================

::

    from django import forms
    from django.utils.translation import ugettext_lazy as _
    from django.contrib.markup.templatetags.markup import markdown
    from django.db import models

    from feincms.module.page.models import Page
    from feincms.admin.item_editor import ItemEditorForm

    from djhallo.widgets import HalloInput


    class MarkdownContentAdminForm(ItemEditorForm):
        content = forms.CharField(widget=HalloInput(),
            required=False, label=_('text'))


    class MarkdownPageContent(models.Model):

        form = MarkdownContentAdminForm
        feincms_item_editor_form = MarkdownContentAdminForm

        content = models.TextField()

        class Meta:
            abstract = True

        def render(self, **kwargs):
            return markdown(self.content)

    Page.create_content_type(MarkdownPageContent)
