=============================
django-exorole
=============================

.. image:: https://badge.fury.io/py/django-exorole.svg
    :target: https://badge.fury.io/py/django-exorole

.. image:: https://travis-ci.org/exolever/django-exorole.svg?branch=master
    :target: https://travis-ci.org/exolever/django-exorole

.. image:: https://codecov.io/gh/exolever/django-exorole/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/exolever/django-exorole

.. image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
   :target: https://github.com/exolever/django-exorole/issues

.. image:: https://img.shields.io/badge/License-MIT-green.svg
   :target: https://opensource.org/licenses/MIT


Use roles system with Django

Quickstart
----------

Install django-exorole::

    pip install django-exorole

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'exo_role',
        ...
    )

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
