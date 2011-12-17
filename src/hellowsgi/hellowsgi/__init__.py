"""
basic wsgi hello world for app engine
"""
from google.appengine.ext.webapp.util import run_wsgi_app


def hello_world(environ, start_response):
    """
    read all about it here
    http://webpython.codepoint.net/wsgi_application_interface
    """
    environ_body = "\n".join(["%s: %s" % (k, v)for k, v in environ.items()])
    body = "Hello App Engine this is WSGI.\n\n %s" % environ_body
    status = "200 OK"
    content_length = len(body)
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(content_length))]
    start_response(status, response_headers)

    return [body]


def main():
    run_wsgi_app(hello_world)

if __name__ == '__main__':
    main()
