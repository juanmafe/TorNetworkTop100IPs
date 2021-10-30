# This file is part of top-100-ips-tor.
# Author: @juanmafe.
# GPLv3 2021.

import os
from copyfile import copyingFiles
from readfile import readingRawFile
from searchfiles import searchingForFiles

def classifyingIps(dirPath, targetFileRaw):

	fileNames = searchingForFiles(os.listdir(dirPath))

	for filename in fileNames:
		copyingFiles(dirPath + filename, dirPath + targetFileRaw)

	return readingRawFile(dirPath + targetFileRaw)

#EOF