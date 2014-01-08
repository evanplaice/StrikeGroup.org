"""@handlers
Handlers for the site

The glue that binds static routes to their corresponding dynamic functionality.
"""

import logging
import base64
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import security

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

  def render_template(self, _template, **context):
    self.response.write(self.jinja2.render_template(_template, **context))


class StaticHandler(BaseHandler):
  """Handles all calls to static pages

  Where dynamic page generation is not needed, this simply loads the static
  html templates as-is.
  """

  def get(self, **kwargs):
    self.render_template(kwargs.get('_uri','/'), nav=urls.nav)
    logging.debug('StaticHandler: ' + kwargs.get('_uri','/'))


class AuthHandler(BaseHandler):
  def password(self):
    password = 'shit';
    return self.secure(password)

  def secure(self, password):
    return security.hash_password(password, method='sha1')

  def login(self):
    self.response.headers['WWW-Authenticate'] = 'Basic realm="Secure Area"'
    self.response.set_status(401, message="Authorization Required")

  def get(self, **kwargs):
    if not 'Authorization' in self.request.headers:
      self.login();
    else:
      auth = self.request.headers['Authorization']
      (username, password) = base64.b64decode(auth.split(' ')[1]).split(':')
      # Check the username and password, and proceed ...
      password = self.secure(password)
      if(self.password() == password):
        logging.info('success')
        logging.info('pass:' + password);
        logging.info('pass:' + self.password());
      else:
        logging.info('fail')
        logging.info('pass:' + password);
        logging.info('pass:' + self.password());
        self.login();