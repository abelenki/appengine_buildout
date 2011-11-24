=================================
 CincyPy App Engine Presentation
=================================

Environment Setup
=================

Because appengine applications are structured in a certain way, this
buildout is being provided to get your environment setup as quickly
and painlessly as possible.

Requirements
------------

Every effort has been made to reduce the requirements to get the
environment initially setup however, the list of requirements is not
zero.

1. An internet connection
2. python verion 2.5 installed
3. 10 fingers

Installing Python 2.5
---------------------

This is operating system specific. And getting to be more and more of
a challenge as time passes. However, eventually Google will be moving
to 2.7 which will make this step unnecessary. Currently 2.7 is
experimental so we're getting close.

Debian/Ubuntu Linux
~~~~~~~~~~~~~~~~~~~

http://welcometoubuntu.blogspot.com/2010/05/howto-install-python-255-on-ubuntu-1004.html

OSX and windows
~~~~~~~~~~~~~~~
http://www.activestate.com/activepython/downloads


Setting things up
-----------------

Once python2.5 is installed, getting your environment setup is as easy
as running these 2 commands.

This command downloads and install buildout to use distribute(rather
  than setuptools) locally to your environment, not system wide.

  $ /path/to/python2.5 bootstrap.py --distribute


This command processes buildout.cfg to download the appengine sdk, any
dependencies you application requires and sets up the application
deployment structure, as well as all the commands you will typically
need. I have included the dpendencies for unit tests as well such as
nose and the nosegae plugin.

  $ ./bin/buildout


Running the app
---------------

After ./bin/buildout has been run successfully you can run the
application locally by running this command.

  $ ./bin/devappserver parts/app

This will launch the development app server on localhost port 8080. To
access it from your web browser go to http://localhost:8080 and you
should see the message "Hello World". 

