"""
Flask-OSS
-------------
Easily serve your static files from aliyun oss.
"""
from setuptools import setup


__version__ = "0.2.2"


setup(
    name="Flask-OSS",
    version=__version__,
    url="https://github.com/edison7500/flask-oss",
    license="Apache",
    author="jiaxin",
    author_email="jiaxin@guoku.com",
    description="Seamlessly serve the static files of your Flask app from aliyun oss",
    long_description=__doc__,
    py_modules=["flask_oss"],
    zip_safe=False,
    include_package_data=True,
    platforms="flask",
    install_requires=["Flask", "oss2>=2.0.0", "six"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
