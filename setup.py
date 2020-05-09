"""
Flask-OSS
-------------
Easily serve your static files from aliyun oss.
"""
import os
import re
from setuptools import setup


def parse_version(asignee):
    here = os.path.dirname(os.path.abspath(__file__))
    version_re = re.compile(r"%s = (\(.*?\))" % asignee)
    with open(os.path.join(here, "flask_oss.py")) as fp:
        for line in fp:
            match = version_re.search(line)
            if match:
                version = eval(match.group(1))
                return ".".join(map(str, version))
        else:
            raise Exception("cannot find version")


version = parse_version("__version__")


setup(
    name="Flask-OSS",
    version=version,
    url="https://github.com/edison7500/flask-oss",
    license="Apache",
    author="jiaxin",
    author_email="jiaxin@guoku.com",
    description="Seamlessly serve the static files of your Flask app from aliyun oss",
    long_description=__doc__,
    py_modules=["flask_oss"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Flask", "oss2>=2.0.0", "six"],
    tests_require=["nose", "mock"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite="nose.collector",
)
