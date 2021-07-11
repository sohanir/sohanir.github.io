#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Sohani Rao'
SITENAME = 'Sincerely Sohani'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken",
    "cover": "images/sohani.png",
    "image": "images/sohani.png",
    "website": "http://sohanir.github.io",
    "location": "US",
    "bio": "Trying cool things with Pelican!"
  }
}

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
LOAD_CONTENT_CACHE = False
USE_FOLDER_AS_CATEGORY = True
STATIC_PATHS = ['images']
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
THEME = '/Library/Python/3.8/site-packages/pelican/themes/attila'
HEADER_COVER = '/images/sohani.png'
HOME_COVER = '/images/sohani.png'
HEADER_COVERS_BY_TAG = {'peom': '/images/sohani.png'}
HEADER_COVERS_BY_CATEGORY = {'poem': '/images/sohani.png'}
HEADER_COLOR = 'black'
COLOR_SCHEME_CSS = 'monokai.css'

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = [
  'pelican-plugins'
]

JINJA_ENVIRONMENT = {
  'extensions' :[
    'jinja2.ext.loopcontrols',
    'jinja2.ext.i18n',
    'jinja2.ext.with_',
    'jinja2.ext.do'
  ]
}

JINJA_FILTERS = {'max': max}