"""@auth
A basic HTTP authorization module

This module handles the most basic http based authorization schemes.
Note, This form of handling logins provices only the most rudimentary
security.
"""

import logging

class AuthTest(handle):
  @basicAuth
  def get(self):
    pass;

  def nogo(self):
    # Wrapping in a huge try/except isn't the best approach. This is just
    # an example for how you might do this.
    try:
      # Parse the header to extract a user/password combo.
      # We're expecting something like "Basic XZxgZRTpbjpvcGVuIHYlc4FkZQ=="
      auth_header = self.request.headers['Authorization']

      # Isolate the encoded user/passwd and decode it
      auth_parts = auth_header.split(' ')
      credentials = base64.b64decode(auth_parts[1]).split(':')
      username = credentials[0]
      password = credentials[1]

      logging.info('user:' + username + ' pass:' + password);
      #checkAuth(username, password) # have this call raise an exception if it fails

      #self.response.out.write(template.render('templates/foo.html', {}))

    except Exception, e:
      logging.debug("AuthTest Exception: %s" % (e))

      # Here's how you set the headers requesting the browser to prompt
      # for a user/password:
      self.response.set_status(401, message="Authorization Required")
      self.response.headers['WWW-Authenticate'] = 'Basic realm="Secure Area"'

      # Rendering a 401 Error page is a good way to go...
      self.response.out.write(template.render('401.html', {}))

  def basicAuth(webappRequest, *args, **kwargs):
    # Parse the header to extract a user/password combo.
    # We're expecting something like "Basic XZxgZRTpbjpvcGVuIHYlc4FkZQ=="
    auth_header = webappRequest.request.headers.get('Authorization')

    if auth_header == None:
      webappRequest.response.set_status(401, message="Authorization Required")
      webappRequest.response.headers['WWW-Authenticate'] = 'Basic realm="Kalydo School"'
    else:
      # Isolate the encoded user/passwd and decode it
      auth_parts = auth_header.split(' ')
      user_pass_parts = base64.b64decode(auth_parts[1]).split(':')
      user_arg = user_pass_parts[0]
      pass_arg = user_pass_parts[1]

      if user_arg != "admin" or pass_arg != "foobar":
        webappRequest.response.set_status(401, message="Authorization Required")
        webappRequest.response.headers['WWW-Authenticate'] = 'Basic realm="Secure Area"'
        # Rendering a 401 Error page is a good way to go...
        self.response.out.write(template.render('templates/error/401.html', {}))
      else:
        return func(webappRequest, *args, **kwargs)