"""
    ChannelEngine Channel API

    ChannelEngine API for channels  # noqa: E501

    The version of the OpenAPI document: 2.9.8
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "channelengine-channel-api-client"
VERSION = "2.9.8"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="ChannelEngine Channel API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/channelengine/channel-api-client-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "ChannelEngine Channel API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    ChannelEngine API for channels  # noqa: E501
    """
)
