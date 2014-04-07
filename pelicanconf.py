#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chris Wallace'
SITENAME = u'Home Page of Chris Wallace'
SITEURL = 'notoriouscw.com'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = "theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ( ('Resume', '/files/resume.pdf'),
    ('My CSE Page', 'http://cse.osu.edu/~wallacch'),
    ('Hack.OSU', 'http://www.osuhackathon.org/'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/@notorious_cw'),
        ('LinkedIn', 'https://www.linkedin.com/pub/christopher-wallace/66/830/b88'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
