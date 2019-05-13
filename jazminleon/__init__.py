# flake8: noqa
from __future__ import absolute_import, unicode_literals

# This will make sure the celery app is always imported when
# Django starts so that tasks can use this celery app.
# Without this Django wouldn't know which celery app to use.
# See http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html
from .celery import app as celery_app

__all__ = ('celery_app',)


__version__ = "0.1.0"
__version_info__ = tuple(
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace("-", ".", 1).split(".")
    ]
)