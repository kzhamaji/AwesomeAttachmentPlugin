# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2011 Dan Ordille <dordille@gmail.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

from setuptools import find_packages, setup

extra = {}

try:
    from trac.util.dist  import  get_l10n_js_cmdclass
    cmdclass = get_l10n_js_cmdclass()
    if cmdclass:
        extra['cmdclass'] = cmdclass
        extractors = [
            ('**.py',                'python', None),
            ('**/templates/**.html', 'genshi', None),
        ]
        extra['message_extractors'] = {
            'awesome': extractors,
        }
# i18n is implemented to be optional here
except ImportError:
    pass

setup(
    name='AwesomeAttachmentsPlugin',
    version='0.4',
    author='Dan Ordille',
    author_email='dordille@gmail.com',
    license='BSD 3-Clause',
    description="Files can be attached to tickets from the New Ticket form.",
    packages=find_packages(exclude=['*.tests']),
    package_data={'awesome': [
        'htdocs/css/*.css',
        'htdocs/images/*.png',
        'htdocs/js/*.js',
        'htdocs/messages/*.js',
        'locale/*/LC_MESSAGES/*.mo',
    ]},
    entry_points="""
        [trac.plugins]
        awesome = awesome.awesomeattachments
    """,
    **extra
)
