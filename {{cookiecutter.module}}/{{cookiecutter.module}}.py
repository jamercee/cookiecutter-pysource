#!/usr/bin/env {{cookiecutter.python}}
# vim: set fileencoding=utf-8
# pylint:disable=line-too-long
r""":mod:`{{cookiecutter.module}}` - {{cookiecutter.module_short_description}}
######################################

.. module:: {{cookiecutter.module}}
   :synopsis: {{cookiecutter.module_short_description}}
.. moduleauthor:: {{cookiecutter.author}} <{{cookiecutter.email}}>

Provide a detailed summary of the module. Break down each subsystem and
describe it's operation in detail

Command line options
********************

*usage:* ``{{cookiecutter.module}}  [-?] [-d] ...``

Positional arguments
====================

.. option:: XXX

   Option XXX provides ...

Optional argument:
==================

.. option:: ?, -h, --help

   Display help and exit

.. option:: -d, --debug

   Generate diagnotic logging.

..
   {{cookiecutter.copyright}}"""
# pylint:enable=line-too-long
# ----------------------------------------------------------------------------
# Standard library imports
# ----------------------------------------------------------------------------
import logging
import sys

# ----------------------------------------------------------------------------
# Module level initializations
# ----------------------------------------------------------------------------
__version__    = '{{cookiecutter.release}}'
__author__     = '{{cookiecutter.author}}'
__email__      = '{{cookiecutter.email}}'
__status__     = '(Development | Production | Testing | Migration)'
__copyright__  = '{{cookiecutter.copyright}}'

LOG = logging.getLogger('{{cookiecutter.module}}')


def main():
    r"""main process driver"""
    pass

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('CTRL-C')
        sys.exit(0)
