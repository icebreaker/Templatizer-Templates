#!/usr/bin/env python

__author__		= '%AUTHOR%'
__description__ = '%DESCRIPTION%'
__version__		= (0, 1, 0)
__license__		= '%LICENSE%'

import sys
import os
import logging

def main(argv):
	""" Main """
	if len(argv) < 2:
		print('%NAME% v%d.%d.%d' % __version__)
		print('usage: %s [options]' % os.path.splitext(os.path.basename(argv[0]))[0])
		print('')
		print('Options:')
		print('\t-v, --version\tshows the version number')
		print('\t-d, --debug\tenables debug output')
		return -1

	if '-v' in argv or '--version' in argv:
		print('%d.%d.%d' % __version__) # print version
		return 0

	if argv[1] == '-d' or argv[1] == '--debug':
		argv.pop(1) # remove this item
		logging.basicConfig(level=logging.DEBUG)
	
	return 0

if __name__ == '__main__':
	exit(main(sys.argv))
