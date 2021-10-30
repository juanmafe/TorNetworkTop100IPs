# This file is part of top-100-ips-tor.
# Author: @juanmafe.
# GPLv3 2021.

from datetime import datetime
from readfile import readingIpFile
from writefile import writtingFile
from orderdictionary import sortingReverse

dictionary = {}
fileToRead = '/var/lib/tor/cached-microdesc-consensus'
fileToWrite = "ips-" + str(datetime.now().time()) + ".txt"

def collectingIps(dirPath):

	dictionaryRaw = readingIpFile(fileToRead)
	writtingFile(sortingReverse(dictionaryRaw), dirPath + fileToWrite, False)

	print("New nodes found: " + str(len(dictionaryRaw)))

#EOF