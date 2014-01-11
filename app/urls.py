"""@urls
Site-wide list of urls and their attibutes

Any information about pages that may need to be passed into
the templating engine is specified here.
"""

__author__ = 'Evan Plaice'

main = [
  { 'uri':'about-us',               'url':'/',                        'template':'about-us.html',               'title':'About Us' },
  { 'uri':'strategic-sourcing',     'url':'/strategic-sourcing',      'template':'strategic-sourcing.html',     'title':'Strategic Sourcing' },
  { 'uri':'government-projects',    'url':'/government-projects',     'template':'government-projects.html',    'title':'Government Projects' },
  { 'uri':'commercial-projects',    'url':'/commercial-projects',     'template':'commercial-projects.html',    'title':'Commercial Projects' },
  { 'uri':'information-technology', 'url':'/information-technology',  'template':'information-technology.html', 'title':'Information Technology' },
  { 'uri':'seaport-e',              'url':'/seaport-e',               'template':'seaport-e.html',              'title':'Seaport Enhanced' },
  { 'uri':'careers',                'url':'/careers',                 'template':'careers.html',                'title':'Careers' },
  { 'uri':'contact-us',             'url':'/contact-us',              'template':'contact-us.html',             'title':'Contact Us' }
]

sub = [
  { 'uri':'certifications',         'url':'/certifications',          'template':'certifications.html',         'title':'Certifications' },
  { 'uri':'sourcing-electrical',    'url':'/sourcing-electrical',     'template':'sourcing-electrical.html',    'title':'Sourcing Electrical' },
  { 'uri':'kitting-capabilities',   'url':'/kitting-capabilities',    'template':'kitting-capabilities.html',   'title':'Kitting Capabilities' },
  { 'uri':'usmc',                   'url':'/usmc',                    'template':'usmc.html',                   'title':'USMC Combat Camera' },
  { 'uri':'usmc-newsletter',        'url':'/usmc-newsletter',         'template':'usmc-newsletter.html',        'title':'USMC Combat Camera Newsletter' },
  { 'uri':'dynmcdermott-petroleum', 'url':'/dynmcdermott-petroleum',  'template':'dynmcdermott-petroleum.html', 'title':'DynMcDermott Petroleum Operations' },
  { 'uri':'louis-stokes-medical',   'url':'/louis-stokes-medical',    'template':'louis-stokes-medical.html',   'title':'Louis Stokes Cleveland, VA Medical Center' },
  { 'uri':'detroit-public-schools', 'url':'/detroit-public-schools',  'template':'detroit-public-schools.html', 'title':'Detroit Public Schools' },
  { 'uri':'gulfport-biloxi',        'url':'/gulfport-biloxi',         'template':'gulfport-biloxi.html',        'title':'Gulfport-Biloxi International Airport Runway' }
]

misc = [
  { 'uri':'_typefaces',             'url':'/_typefaces',              'template':'_typefaces.html',             'title':'Typeface Style Guide' },

]

masterlist = main + sub + misc