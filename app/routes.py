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
  Route('/usmc-combat-camera',      StaticHandler, defaults={'_uri':'usmc-combat-camera.html'})]

auth = [
  Route('/usmc/',       AuthHandler),
  Route('/usmc/<_uri>', AuthHandler)]

redirects = [
  Route('/strategic.html',  RedirectHandler, defaults={'_uri':'strategic-sourcing'}),
  Route('/government.html', RedirectHandler, defaults={'_uri':'government-projects'}),
  Route('/commercial.html', RedirectHandler, defaults={'_uri':'commercial-projects'}),
  Route('/it.html',         RedirectHandler, defaults={'_uri':'information-technology'}),
  Route('/location.html',   RedirectHandler, defaults={'_uri':'locations'}),
  Route('/electrical.html', RedirectHandler, defaults={'_uri':'sourcing-electrical'}),
  Route('/comcam.html',     RedirectHandler, defaults={'_uri':'usmc-combat-camera'})]

master = main + auth + redirects