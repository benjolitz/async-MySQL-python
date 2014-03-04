#!/usr/bin/env python

import os
import sys
from setuptools import setup, Extension

if not hasattr(sys, "hexversion") or sys.hexversion < 0x02030000:
    raise Exception("Python 2.3 or newer is required")

if os.name == "posix":
    from setup_posix import get_config
else:  # assume windows
    from setup_windows import get_config

metadata, options = get_config()
# Some distros of mysql don't include hash.h which is an integral part of
# sql_common.h (which defines the correct typedef for struct st_mysql_methods)
# I've duped the missing header from
# https://github.com/twitter/mysql/blob/master/include/hash.h
options['include_dirs'] += \
    [os.path.abspath(os.path.dirname(os.path.abspath(__file__)))]
metadata['ext_modules'] = [Extension(sources=['_mysql.c'], **options)]
metadata['long_description'] = metadata['long_description'].replace(r'\n', '')

setup(**metadata)
