#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Устанавливаем стандартную внешнюю кодировку = utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {'link': u'<a href="about/aboutme.html">Обо мне</a>'}

@view_config(route_name='about', renderer='templates/about/aboutme.jinja2')
def about(request):
    return {'link': u'<a href="/">Домой</a>'}