#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#作者设置
AUTHOR = u'Atlas 晓'
AUTHOR_URL = 'author/{slug}.html'
#AUTHOR_SAVE_AS = False
#AUTHORS_URL = 'authors.html'
#AUTHORS_SAVE_AS = False

#网站设置
SITENAME = u'晓的博客'
SITEURL = 'http://zhangxiaolong.org'

#标签设置
TAG_CLOUD_STEPS = 4
#TAGS_URL = 'tags.html'
#TAGS_SAVE_AS  = False
#TAG_URL = 'tag/{slug}.html'
#TAG_SAVE_AS = False

#分类设置
#DEFAULT_CATEGORY = '主页'
#CATEGORY_URL = 'category/{slug}.html'
#CATEGORY_SAVE_AS = False


DS_SITENAME = u"atlas555"
GOOGLE_ANALYTICS_ID = 'UA-43475675-3'
GOOGLE_ANALYTICS_SITENAME = 'zhangxiaolong.org'
SHARE = True
SHARE_ID = 1875744

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None 


DEFAULT_PAGINATION = 10
#RECENT_POSTS = 10
HOT_POSTS = 10
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#文章存储目录和形式
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
TIMEZONE = 'Asia/Shanghai'
THEME = "atlas"
DEFAULT_LANG = u'zh'
DS_SITENAME = u"atlas555"
GOOLE_ANALYTICS_ID = 'UA-43475675-3'
GOOGLE_ANALYTICS_SITENAME = 'zhangxiaolong.org'
SHARE = True
SHARE_ID = 1875744

#PAGE_DIR = 'pages'
#PAGE_EXCLUDES = ()
#ARTICLE_EXCLUDES =  (('pages'),('extra'),('_gsdata_'))

#静态目录
# static paths will be copied under the same name
STATIC_PATHS = [
	'pictures',
	'extra/robots.txt',
	'extra/.htaccess',
	'extra/CNAME'
	'extra/favicon.ico'
	 ]

# A list of files to copy from the source to the destination

# custom page generated with a jinja2 template
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/.htaccess': {'path': '.htacess'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }
#TEMPLATE_PAGES = {'pages/jinja2_template.chtml': 'jinja2_template.html'}
TEMPLATE_PAGES = {
        "404.html": "404.html",
        }

#加载插件
PLUGIN_PATH = u"pelican-plugins"

PLUGINS = ["sitemap","random_article","neighbors","gzip_cache"]

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "weekly",
        "indexes": "daily",
        "pages": "monthly",
    }
}
#随机跳转到某一日志
RANDOM = 'random.html'



