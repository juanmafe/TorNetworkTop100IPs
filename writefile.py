# This file is part of top-100-ips-tor.
# Author: @juanmafe.
# GPLv3 2021.

def writtingFile(dictionary, file, withlimit):

	fileToWrite = open(file, "w+")
	counterLine = 0

	for ip, velocity in dictionary.items():
		field = '{:20}'.format(ip) + ' : ' + str(velocity) + '\n'
		fileToWrite.write(field)
		counterLine += 1

		if (withlimit and counterLine == 100):
			break

	fileToWrite.close()

#EOF