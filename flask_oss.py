# -*- coding: utf-8 -*-
import logging

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

import oss2
import oss2.exceptions


logger = logging.getLogger('flask_oss')


__version__ = (0, 1, 0)



class FlaskOSS(object):


    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        _access_key     = app.config.get('OSS_ACCESS_KEY_ID')
        _secret         = app.config.get('OSS_SECRET_ACCESS_KEY')
        _endpoint       = app.config.get('OSS_ENDPOINT')
        _bucket_name    = app.config.get('OSS_BUCKET_NAME')
        # assert self.access_key is not None
        # print self.access_key
        # if self.access_key is None or self.secret is None:
        #     raise
        self.auth   = oss2.Auth(_access_key, _secret)

        self.bucket = oss2.Bucket(self.auth, _endpoint, _bucket_name)


    def get_file(self, filename=None):
        assert filename is not None

        try:
            result = self.bucket.get_object(filename)
            return result.read()
        except oss2.exceptions.NoSuchKey as e:
            logger.error('{0} not found: http_status={1}, request_id={2}'.format(filename, e.status, e.request_id))



if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)
    app.config['OSS_ACCESS_KEY_ID']     = 'kj7wLAH8ABFz75Ok'
    app.config['OSS_SECRET_ACCESS_KEY'] = '7c0TZc3ZkLzEPTDJ4Z4jzuxJkze9ZC'
    app.config['OSS_ENDPOINT']          = 'oss.aliyuncs.com'
    app.config['OSS_BUCKET_NAME']       = 'epub360-media'
    oss = FlaskOSS(app)

    print oss.get_file('materials/origin/a95ab572aa805d743fce5a0e45957054_origin.png')
    # print oss


    # def auth(self):



