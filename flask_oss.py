# -*- coding: utf-8 -*-
import logging
import oss2
import oss2.exceptions

logger = logging.getLogger("flask_oss")


class FlaskOSS(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        _access_key = app.config.get("OSS_ACCESS_KEY_ID")
        _secret = app.config.get("OSS_SECRET_ACCESS_KEY")
        _endpoint = app.config.get("OSS_ENDPOINT")
        _bucket_name = app.config.get("OSS_BUCKET_NAME")

        self.auth = oss2.Auth(_access_key, _secret)
        self.bucket = oss2.Bucket(self.auth, _endpoint, _bucket_name)

    def put_file(self, filename=None, raw_contents=None):
        success = self.bucket.put_object(filename, raw_contents)
        if success.status == 200:
            return filename
        else:
            logger.error(f"FAILURE writing file {filename}")

    def put_file_by_path(self, filename=None, filepath=None):
        """
        :param filename: filename-in-oss.txt
        :param filepath: /tmp/folder/filename-in-local.txt
        :return: filename
        """
        success = self.bucket.put_object_from_file(filename, filepath)
        if success.status == 200:
            return filename
        else:
            logger.error(f"FAILURE writing file {filename}")

    def get_file(self, filename=None):
        try:
            result = self.bucket.get_object(filename)
            return result.read()
        except oss2.exceptions.NoSuchKey as e:
            logger.error(
                f"{filename} not found: http_status={e.status}, request_id={e.request_id}"
            )

    def exists_file(self, filename=None):
        exist = self.bucket.object_exists(filename)
        if exist:
            return True

    def del_file(self, filename=None):
        is_delete = False
        try:
            self.bucket.delete_object(filename)
            is_delete = True
        except oss2.exceptions.NoSuchKey as e:
            logger.error(
                f"{filename} not found: http_status={e.status}, request_id={e.request_id}"
            )
        return is_delete
