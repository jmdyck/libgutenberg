#!/usr/bin/env python
#  -*- mode: python; indent-tabs-mode: nil; -*- coding: iso-8859-1 -*-

"""
MediaTypes.py

Copyright 2009 by Marcello Perathoner

Distributable under the GNU General Public License Version 3 or newer.

Media Types Lists

"""

from __future__ import unicode_literals

E2T = dict ()
T2E = dict ()

for ext, mimetype in (
        ('atom',    'application/atom+xml'),
        ('css',     'text/css'),
        ('epub',    'application/epub+zip'),
        ('gif',     'image/gif'),
        ('htm',     'text/html'),
        ('html',    'text/html'),
        ('jar',     'application/java-archive'),
        ('jpeg',    'image/jpeg'),
        ('jpg',     'image/jpeg'),
        ('js',      'application/javascript'),
        ('json',    'application/x-suggestions+json'),
        ('marc',    'application/marc'),
        ('mobi',    'application/x-mobipocket-ebook'),
        ('mobile',  'application/xhtml+xml'),
        ('ncx',     'application/x-dtbncx+xml'),
        ('opds',    'application/atom+xml'),
        ('pdf',     'application/pdf'),
        ('pdb',     'application/prs.plucker'),
        ('plucker', 'application/prs.plucker'),
        ('png',     'image/png'),
        ('pt',      'application/vnd.adobe-page-template+xml'),
        ('qioo',    'application/x-qioo-ebook'),
        ('rdf',     'application/rdf+xml'),
        ('rss',     'application/rss+xml'),
        ('rst',     'text/x-rst'),
        ('stanza',  'application/atom+xml'),
        ('txt',     'text/plain'),
        ('wap',     'application/vnd.wap.xhtml+xml'),
        ('xhtml',   'application/xhtml+xml'),
        ('xml',     'application/xml'),
):
    T2E[mimetype] = ext
    E2T[ext] = mimetype

TEXT_MEDIATYPES = set ( (
    'application/xhtml+xml',
    'application/xml',
    'text/html',
    'text/plain',
    'text/x-rst',
) )

IMAGE_MEDIATYPES = set ( (
    'image/gif',
    'image/jpeg',
    'image/png',
) )

AUX_MEDIATYPES = set ( (
    'text/css',
) )


def guess_type (url):
    """ Guess the mimetype of an url. """

    ext = url.split ('.')[-1]
    return E2T[ext.lower ()]


class MediatypesLookup (object):
    """ Quick mediatype lookup

    >>> ns = MediatypesLookup ()
    >>> ns.epub
    'application/epub+zip'
    >>> ns['mobi']
    'application/x-mobipocket-ebook'

    """

    def __getitem__ (self, local):
        return guess_type (local)

    def __getattr__ (self, local):
        return guess_type (local)


mediatypes = MediatypesLookup ()
