# -*- coding: utf-8 -*-
"""

test_utils.py
=============

Helpers for testing django applications.

"""

from __future__ import with_statement
from django.conf import settings, UserSettingsHolder
from django.utils.functional import wraps

# Grabbed from: http://djangosnippets.org/snippets/2437/
class override_settings(object):
    """
    Acts as either a decorator, or a context manager.  If it's a decorator it
    takes a function and returns a wrapped function.  If it's a contextmanager
    it's used with the ``with`` statement.  In either event entering/exiting
    are called before and after, respectively, the function/block is executed.
    """
    def __init__(self, **kwargs):
        self.options = kwargs
        self.wrapped = settings._wrapped

    def __enter__(self):
        self.enable()

    def __exit__(self, exc_type, exc_value, traceback):
        self.disable()

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return inner

    def enable(self):
        override = UserSettingsHolder(settings._wrapped)
        for key, new_value in self.options.items():
            setattr(override, key, new_value)
        settings._wrapped = override

    def disable(self):
        settings._wrapped = self.wrapped

# Grabbed from http://djangosnippets.org/snippets/1875/
# Put this in any models module
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals

# From http://stackoverflow.com/questions/1466827/ --
#
# Prevent interactive question about wanting a superuser created.  (This code
# has to go in this otherwise empty "models" module so that it gets processed by
# the "syncdb" command during database creation.)
signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')


# Create our own test user automatically.

def create_testuser(app, created_models, verbosity, **kwargs):
  if not settings.DEBUG:
    return
  try:
    auth_models.User.objects.get(username='test')
  except auth_models.User.DoesNotExist:
    print '*' * 80
    print 'Creating test user -- login: test, password: t'
    print '*' * 80
    assert auth_models.User.objects.create_superuser('test', 'x@x.com', 't')
  else:
    print 'Test user already exists.'

signals.post_syncdb.connect(create_testuser,
    sender=auth_models, dispatch_uid='common.models.create_testuser')
