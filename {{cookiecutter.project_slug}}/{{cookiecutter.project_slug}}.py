#!/usr/bin/env {{cookiecutter.python}}
# vim: set fileencoding=utf-8
# pylint:disable=line-too-long
r""":mod:`@module@` - {{cookiecutter.module_short_description}}
#######################################

.. module:: @module@
   :synopsis: {{cookiecutter.module_short_description}}
.. moduleauthor:: @author@ <@email@>

Provide a detailed summary of the module Break down each subsystem and describe
it's operation in detail

Command line options
********************

*usage:* ``@module@  [-?] [-d] ...``

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
   @copyright@"""
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
__author__     = '@author@'
__email__      = '@email@'
__status__     = '(Development | Production | Testing | Migration)'
__copyright__  = '@copyright@'

LOG = logging.getLogger('@module@')


def main():
    r"""main process driver"""
    pass

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('CTRL-C')
        sys.exit(0)
