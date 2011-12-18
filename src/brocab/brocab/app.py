"""
brocab application defined here
"""
from pyramid.configuration import Configurator
from pyramid import httpexceptions as htex
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.appstats import recording
import os

here = os.path.dirname(os.path.abspath(__file__))


class Word(db.Model):
    """
    schema for word
    """
    value = db.StringProperty(required=True)
    definition = db.TextProperty(required=True)


def view_form(request):
    """
    create and edit words
    """
    response = None

    if "POST" in request.params:
        # handle form post (would validate input here)
        _id, value, definition = request.POST.get("id"), \
                                request.POST.get("value"), \
                                request.POST.get("definition")

        if _id:
            # edit existing
            w = Word.get_by_id(int(_id))
            if not w:
                response = htex.HTTPNotFound(_id)
            else:
                w.value = value
                w.definition = definition
        else:
            #create new word
            w = Word(value=value, definition=definition)
        w.put()

        #always redirect to avoid form double post problem
        response = htex.HTTPFound(location="/index.html")
    else:
        #render form
        if "_id" in request.params:
            # edit word
            w = Word.get_by_id(int(request.params["_id"]))
            if w:
                response = dict(id=w.key().id(), value=w.value,
                                definition=w.definition)
            else:
                response = htex.HTTPNotFound(request.params["_id"])
        else:
            # create new word
            response = dict(id=None, value=None, definition=None)

    if response:
        return response
    else:
        raise ValueError("We missed some condition somewhere")


def view_index(request):
    """
    word list
    """
    return dict(words=list(Word.all()))


def view_root(request):
    """
    handles redirect to index.html from / like servers are supposed to
    """
    return htex.HTTPFound(location="/index.html")


def make_app():
    """
    initialize application views and return a wsgi app
    """
    # tell mako to look in the templates directory
    settings = {"mako.directories": os.path.join(here, "templates")}
    #initialize pyramid with settings
    config = Configurator(settings=settings)
    #add root view, called when /
    config.add_view(view_root)
    #add index view, called when index.html
    config.add_view(view_index, name="index.html", renderer="index.mako")
    #add edit view, called when edit.html
    config.add_view(view_form, name="edit.html", renderer="form.mako")
    return config.make_wsgi_app()


def main():
    """
    when request is recieved, run wsgi application
    """
    run_wsgi_app(recording.appstats_wsgi_middleware(make_app()))

if __name__ == '__main__':
    main()
