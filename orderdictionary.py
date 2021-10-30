# This file is part of top-100-ips-tor.
# Author: @juanmafe.
# GPLv3 2021.

def sortingReverse(dictionary):
	return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse = True))

#EOF