"""@routes
Route configurations for the site

The sub-lists make up the different sections of the site. Generate a master
list by combining them at the bottom.
"""

__author__ = 'Evan Plaice'

from webapp2 import Route, RedirectHandler
from handlers import StaticHandler

static = [
  Route('/',                        StaticHandler,  defaults={'_uri':'about-us'}),
  Route('/strategic-sourcing',      StaticHandler,  defaults={'_uri':'strategic-sourcing'}),
  Route('/government-projects',     StaticHandler,  defaults={'_uri':'government-projects'}),
  Route('/commercial-projects',     StaticHandler,  defaults={'_uri':'commercial-projects'}),
  Route('/information-technology',  StaticHandler,  defaults={'_uri':'information-technology'}),
  Route('/locations',               StaticHandler,  defaults={'_uri':'locations'}),
  Route('/careers',                 StaticHandler,  defaults={'_uri':'careers'}),
  Route('/contact-us',              StaticHandler,  defaults={'_uri':'contact-us'}),
  Route('/certifications',          StaticHandler,  defaults={'_uri':'certifications'}),
  Route('/sourcing-electrical',     StaticHandler,  defaults={'_uri':'sourcing-electrical'}),
  Route('/kitting-capabilities',    StaticHandler,  defaults={'_uri':'kitting-capabilities'}),
  Route('/usmc',                    StaticHandler,  defaults={'_uri':'usmc'}),
  Route('/usmc-newsletter',         StaticHandler,  defaults={'_uri':'usmc-newsletter'}),
  Route('/dynmcdermott-petroleum',  StaticHandler,  defaults={'_uri':'dynmcdermott-petroleum'}),
  Route('/shiprider-program',       StaticHandler,  defaults={'_uri':'shiprider-program'}),
  Route('/louis-stokes-medical',    StaticHandler,  defaults={'_uri':'louis-stokes-medical'}),
  Route('/seaport-e',               StaticHandler,  defaults={'_uri':'seaport-e'}),
  Route('/detroit-public-schools',  StaticHandler,  defaults={'_uri':'detroit-public-schools'}),
  Route('/gulfport-biloxi',         StaticHandler,  defaults={'_uri':'gulfport-biloxi'}),
  Route('/_typefaces',              StaticHandler,  defaults={'_uri':'_typefaces'}),
  Route('/_pdf',                    StaticHandler,  defaults={'_uri':'_pdf'}),
]

redirects = [
  Route('/private',             RedirectHandler,  defaults={'_uri':'/private/'}),
  Route('/index.html',          RedirectHandler,  defaults={'_uri':'/'}),
  Route('/strategic.html',      RedirectHandler,  defaults={'_uri':'/strategic-sourcing'}),
  Route('/Government.html',     RedirectHandler,  defaults={'_uri':'/government-projects'}),
  Route('/commercial.html',     RedirectHandler,  defaults={'_uri':'/commercial-projects'}),
  Route('/it.html',             RedirectHandler,  defaults={'_uri':'/information-technology'}),
  Route('/location.html',       RedirectHandler,  defaults={'_uri':'/locations'}),
  Route('/certifications.html', RedirectHandler,  defaults={'_uri':'/certifications'}),
  Route('/electrical.html',     RedirectHandler,  defaults={'_uri':'/sourcing-electrical'}),
  Route('/comcam.html',         RedirectHandler,  defaults={'_uri':'/usmc'})
]

masterlist = static + redirects
