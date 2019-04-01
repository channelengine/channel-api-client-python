# coding: utf-8

"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "channelengine-channel-api-client"
VERSION = "2.7.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="ChannelEngine Channel API",
    author_email="",
    url="https://github.com/channelengine/channel-api-client-python",
    keywords=["Swagger", "ChannelEngine Channel API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    ChannelEngine API for channels  # noqa: E501
    """
)
