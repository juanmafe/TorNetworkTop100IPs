# This script is a utility to collecting and classify Tor IPs.
# Based on Kirzahk's version.
# Author: @juanmafe.
# GPLv3 2021.

import os
from writefile import writtingFile
from ipscollector import collectingIps
from ipclassificator import classifyingIps
from orderdictionary import sortingReverse

dirPath = "ips/"
targetFileRaw = "rawIps.txt"
targetFileFinal = "finalIps.txt"

if not (os.path.exists(dirPath)):
	os.mkdir(dirPath)

collectingIps(dirPath)

if not (os.path.exists(dirPath + targetFileRaw)):
	os.mknod(dirPath + targetFileRaw)

if not (os.path.exists(dirPath + targetFileFinal)):
	os.mknod(dirPath + targetFileFinal)

writtingFile(sortingReverse(classifyingIps(dirPath, targetFileRaw)), dirPath + targetFileFinal, True)

if os.path.exists(dirPath + targetFileRaw):
	os.remove(dirPath + targetFileRaw)

#EOF