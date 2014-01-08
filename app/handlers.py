"""@handlers
Handlers for the site

The glue that binds static routes to their corresponding dynamic functionality.
"""

__author__ = 'Evan Plaice'

import os
import logging
import base64
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import security
import yaml

import urls

class BaseHandler(webapp2.RequestHandler):
  """The base class for all calls to the templating engine

  This class sets up the initial configuration for jinja2 and makes
  rendering possible in subclasses. It can be called on it's own but
  it's designed to be inherited.
  """

  @webapp2.cached_property
  def jinja2(self):
    j = jinja2.get_jinja2(app=self.app)
    #j.environment.filters.update({
        # Set filters.
        # ...
    #})
    #j.environment.globals.update({
        # Set global variables.
        #'uri_for': webapp2.uri_for,
    #})
    return j

  def render_template(self, template, **context):
    self.response.write(self.jinja2.render_template(template, **context))

  def init(self, **params):
    if hasattr(self, 'context') and hasattr(self, 'meta'):
      return
    self.context = {}
    for url in urls.masterlist:
      if url['uri'] == params.get('_uri','/'):
        self.meta = url
        break

  def get(self, **params):
    self.render_template(self.meta['template'], **self.context)
    logging.debug('Rendering: ' + self.meta['template'])

class StaticHandler(BaseHandler):
  """Handles all calls to static pages

  Where dynamic page generation is not needed, this simply loads the static
  html templates as-is.
  """

  def get(self, **params):
    self.init(**params)
    self.context['title'] = self.meta['title']
    self.context['nav'] = urls.main
    BaseHandler.get(self, **params)