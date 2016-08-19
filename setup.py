#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Setuptools installer for Twisted.
"""

import os
import sys
import setuptools


# Tell Twisted not to enforce zope.interface requirement on import, since
# we're going to have to import twisted.python._setup and can rely on
# setuptools to install dependencies.
setuptools._TWISTED_NO_CHECK_REQUIREMENTS = True

if __name__ == "__main__":
    from twisted.python._setup import get_setup_args
    try:
        if os.path.exists('src/twisted/'):
            sys.path.insert(0, 'src')
        setuptools.setup(**get_setup_args())
    except KeyboardInterrupt:
        sys.exit(1)
