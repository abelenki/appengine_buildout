"""
hello world webob version
"""
from google.appengine.ext.webapp.util import run_wsgi_app
from webob import Response


def hello_world(environ, start_response):
    """
    read all about it here
    http://docs.webob.org/en/latest/reference.html
    """
    environ_body = "\n".join(["%s: %s" % (k, v)for k, v in environ.items()])
    body = "Hello App Engine this is webob.\n\n %s" % environ_body
    res = Response(body)
    res.content_type = "text/plain"
    return res(environ, start_response)


def main():
    run_wsgi_app(hello_world)

if __name__ == '__main__':
    main()
