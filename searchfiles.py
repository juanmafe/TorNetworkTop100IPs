# This file is part of top-100-ips-tor.
# Author: @juanmafe.
# GPLv3 2021.

def searchingForFiles(files):

	fileNames = []

	for file in files:
		if file[-4:] == '.txt' and file[-7:] != 'Ips.txt':
			fileNames.append(file)
	return fileNames

#EOF