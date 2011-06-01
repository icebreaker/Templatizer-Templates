#!/usr/bin/env python
from distutils.core import setup
import %FILENAME%

setup(
	name='%FILENAME%',
	version='%d.%d.%d' % %FILENAME%.__version__,
	description=%FILENAME%.__description__,
	author=%FILENAME%.__author__,
	scripts=['bin/%FILENAME%'],
	py_modules=['%FILENAME%'],
	classifiers=[
		'Development Status :: 1 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: FSF Approved :: %LICENSE% License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Utilities'
    ],
)
