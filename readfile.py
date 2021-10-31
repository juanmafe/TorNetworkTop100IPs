# This file is part of top-100-ips-tor.
# Author: @juanmafe.
# GPLv3 2021.

def readingIpFile(file):

	dictionary = {}
	fileToRead = open(file)

	for line in fileToRead:
		line = line.rstrip()

		if line.startswith("r "):
			lineR = line.split(' ')
			directionIP = lineR[5]

		if line.startswith("w "):
			lineW = line.replace('w Bandwidth=','')
			dictionary[directionIP] = int(lineW.split(' ')[0])

	fileToRead.close
	return dictionary


def readingRawFile(file):

	dictionary = {}
	fileToRead = open(file)

	for line in fileToRead:
		line = line.rstrip()

		lineReplaced = line.replace(' ','')
		lineSplitted = lineReplaced.split(":")

		if lineSplitted[0] in dictionary and dictionary.get(lineSplitted[0]) < int(lineSplitted[1]):
			dictionary.update({lineSplitted[0] : int(lineSplitted[1])})

		if not lineSplitted[0] in dictionary:
			dictionary[lineSplitted[0]] = int(lineSplitted[1])

	fileToRead.close
	return dictionary

#EOF