from webob import Response
from google.appengine.ext.webapp.util import run_wsgi_app
application = Response("Hello World")
run_wsgi_app(application)
