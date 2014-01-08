"""@main
The canonical entry point for this web application.

This is the heart of the application. As soon as the application variable is
set the site will launches so set any application-wide variables/configuration
above that call.
"""

import webapp2
import logging
import routes

#logging.getLogger().setLevel(logging.DEBUG)
application = webapp2.WSGIApplication(routes.master, debug=False)