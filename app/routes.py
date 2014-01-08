"""@routes
Route configurations for the site

The sub-lists make up the different sections of the site. Generate a master
list by combining them at the bottom.
"""

from webapp2 import Route, RedirectHandler
from handlers import StaticHandler, AuthHandler
from decorators import ClassProperty

main = [
  Route('/',                        StaticHandler, defaults={'_uri':'index.html'}),
  Route('/about-us',                StaticHandler, defaults={'_uri':'index.html'}),
  Route('/strategic-sourcing',      StaticHandler, defaults={'_uri':'strategic-sourcing.html'}),
  Route('/government-projects',     StaticHandler, defaults={'_uri':'government-projects.html'}),
  Route('/commercial-projects',     StaticHandler, defaults={'_uri':'commercial-projects.html'}),
  Route('/information-technology',  StaticHandler, defaults={'_uri':'information-technology.html'}),
  Route('/locations',               StaticHandler, defaults={'_uri':'locations.html'}),
  Route('/certifications',          StaticHandler, defaults={'_uri':'certifications.html'}),
  Route('/sourcing-electrical',     StaticHandler, defaults={'_uri':'sourcing-electrical.html'}),
  Route('/usmc',      StaticHandler, defaults={'_uri':'usmc.html'})]

auth = [
  Route('/private/',       AuthHandler),
  Route('/private/<_uri>', AuthHandler)]

redirects = [
  Route('/index.html',          RedirectHandler,  defaults={'_uri':'/'}),
  Route('/strategic.html',      RedirectHandler,  defaults={'_uri':'strategic-sourcing'}),
  Route('/Government.html',     RedirectHandler,  defaults={'_uri':'government-projects'}),
  Route('/commercial.html',     RedirectHandler,  defaults={'_uri':'commercial-projects'}),
  Route('/it.html',             RedirectHandler,  defaults={'_uri':'information-technology'}),
  Route('/location.html',       RedirectHandler,  defaults={'_uri':'locations'}),
  Route('/certifications.html', RedirectHandler,  defaults={'_uri':'certifications'}),
  Route('/electrical.html',     RedirectHandler,  defaults={'_uri':'sourcing-electrical'}),
  Route('/comcam.html',         RedirectHandler,  defaults={'_uri':'usmc'})]

master = main + auth + redirects