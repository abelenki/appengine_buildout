"""
brocab application defined here
"""
from pyramid.configuration import Configurator
from pyramid import httpexceptions as htex
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import os

here = os.path.dirname(os.path.abspath(__file__))


class Word(db.Model):
    value = db.StringProperty(required=True)
    definition = db.TextProperty()


def view_form(request):
    if "POST" in request.params:
        _id, value, definition = request.POST.get("id"), \
                                request.POST.get("value"), \
                                request.POST.get("definition")
        if _id:
            w = Word.get_by_id(int(_id))
            if not w:
                raise htex.HTTPNotFound(_id)
            else:
                w.value = value
                w.definition = definition
        else:
            w = Word(value=value, definition=definition)
        w.put()
        return htex.HTTPFound(location="/")
    else:
        if "_id" in request.params:
            w = Word.get_by_id(int(request.params["_id"]))
            return dict(id=w.key().id(), value=w.value, definition=w.definition)
        else:
            return dict(id=None, value=None, definition=None)


def view_index(request):
    return dict(words=Word.all())


def make_app():
    settings = {"mako.directories": os.path.join(here, "templates")}
    config = Configurator(settings=settings)
    config.add_view(view_index, renderer="index.mako")
    config.add_view(view_form, name="edit", renderer="form.mako")
    return config.make_wsgi_app()


def main():
    run_wsgi_app(make_app())

if __name__ == '__main__':
    main()
