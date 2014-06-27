# encoding=utf-8

import os
import sys
import wsgiref.handlers

from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext.webapp import template

import handlers
import webapp2

sys.path.insert(0, os.path.dirname(__file__))
template.register_template_library('templatetags.filters')
app = webapp2.WSGIApplication(handlers.handlers)