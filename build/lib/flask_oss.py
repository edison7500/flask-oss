# -*- coding: utf-8 -*-
import hashlib
import json
import logging
import os
import re
import gzip

import warnings

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import mimetypes
from collections import defaultdict

import oss2
import oss2.exceptions
from oss2.exceptions import ClientError
from flask import current_app
from flask import url_for as flask_url_for
import six


logger = logging.getLogger('flask_oss')


DEFAULT_SETTINGS = {'FLASKOSS_USE_HTTPS': True,
                    'FLASKOSS_ACTIVE': True,
                    'FLASKOSS_DEBUG': False,
                    'FLASKOSS_BUCKET_DOMAIN': 's3.amazonaws.com',
                    'FLASKOSS_CDN_DOMAIN': '',
                    'FLASKOSS_USE_CACHE_CONTROL': False,
                    'FLASKOSS_HEADERS': {},
                    'FLASKOSS_FILEPATH_HEADERS': {},
                    'FLASKOSS_ONLY_MODIFIED': False,
                    'FLASKOSS_URL_STYLE': 'host',
                    'FLASKOSS_GZIP': False,
                    'FLASKOSS_GZIP_ONLY_EXTS': [],
                    'FLASKOSS_FORCE_MIMETYPE': False,
                    }

__version__ = (0, 1, 0)



class FlaskOSS(object):


    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        An alternative way to pass your :class:`flask.Flask` application
        object to Flask-S3. :meth:`init_app` also takes care of some
        default `settings`_.
        :param app: the :class:`flask.Flask` application object.
        """

        for k, v in DEFAULT_SETTINGS.items():
            app.config.setdefault(k, v)

