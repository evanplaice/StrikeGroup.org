"""@main
The canonical entry point for this web application.

This is the heart of the application. As soon as the application variable is
set the site will launches so set any application-wide variables/configuration
above that call.
"""

__author__ = 'Evan Plaice'

import os
import webapp2
import logging
import routes

# Detect whether this the 'Development' server
DEV = os.environ['SERVER_SOFTWARE'].startswith('Dev')

# Enable logging on the 'Development' server
if(DEV):
  logging.getLogger().setLevel(logging.DEBUG)
else:
  logging.getLogger().setLevel(logging.CRITICAL)

application = webapp2.WSGIApplication(routes.masterlist, debug=False)