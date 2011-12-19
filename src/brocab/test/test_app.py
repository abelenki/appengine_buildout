"""
this isn't unit tests, these are functional tests in that we are
sending actual requests to the application and evaluating whether we
are getting the correct response

http://webtest.pythonpaste.org/en/latest/index.html


cmd to run: cd ~/projects/appengine_presentation/ ; ./bin/nosetests -x --with-gae --gae-application=parts/brocab-app/ src/brocab/test/test_app.py
"""
import unittest
from webtest import TestApp
from brocab.app import make_app, Word, db
import string


class TestStatusCodes(unittest.TestCase):
    def setUp(self):
        super(TestStatusCodes, self).setUp()
        self.app = TestApp(make_app())

    def testGetIndexPage(self):
        """
        should return
        """
        self.app.get("/index.html")

    def testGetEditPage(self):
        """
        should return
        """
        self.app.get("/edit.html")

    def testGetRoot(self):
        self.app.get("/", status=302)

    def testEdit404(self):
        """
        since there are no words, should return a 404 when given an id
        """
        self.app.get("/edit.html", dict(_id=1000), status=404)


class TestCrud(unittest.TestCase):
    def setUp(self):
        super(TestCrud, self).setUp()
        self.app = TestApp(make_app())
        test_data = [Word(value="BRO%s" % x, definition="A bro%s" % x) \
                     for x in string.ascii_letters]
        db.put(test_data)
        self.test_data = test_data

    def testList(self):
        """
        check if all test data is accounted for
        """
        res = self.app.get("/index.html")

        for c in self.test_data:
            self.assert_(c.value in res.body, "value %s missing" % c.value)
            self.assert_(c.definition in res.body, "definition %s missing" % c.definition)

    def testCreateNew(self):
        """
        check if create new works
        """
        res = self.app.get("/edit.html")
        form = res.form
        form.set("value", "new bro word")
        form.set("definition", "new bro definition")
        res = form.submit()

        # should get redirected if success
        self.assert_(res.status_int == 302, res.status)

        # new word in the database?
        words = [w for w in Word.all() if w.value == "new bro word"]
        self.assert_(len(words) and words[0])
        #follow redirect
        res = res.follow()
        # check that it shows up on the listing
        res = self.app.get("/index.html")
        self.assert_("new bro word" in res.body, str(res))


    def testEdit(self):
        """
        check that editting words works
        """
        # for each word, edit it and see if it shows up in the listing
        # with the new values
        for w in self.test_data:
            res = self.app.get("/edit.html", dict(_id=w.key().id()))
            form = res.form
            self.assert_(w.value == form["value"].value, form["value"].value)
            self.assert_(w.definition == form["definition"].value,\
                         form["definition"].value)
            self.assert_(str(w.key().id()) == form["id"].value,\
                         form["id"].value)
            new_value = "new bro word %s" % w.value
            new_definition = "new bro definition %s" % w.definition
            form.set("value", new_value)
            form.set("definition", new_definition)
            res = form.submit()
            self.assert_(res.status_int == 302, res.status)
            word = Word.get_by_id(w.key().id())
            self.assert_(word)
            res = res.follow()
            res = self.app.get("/index.html")
            self.assert_(new_value in res.body, str(res))
            self.assert_(new_definition in res.body, str(res))
