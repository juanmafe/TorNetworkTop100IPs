# This file is part of top-100-ips-tor.
# Author: @juanmafe.
# GPLv3 2021.

def copyingFiles(origin, target):

	with open(origin) as fileOrigin:
		with open(target, "a") as fileTarget:
			counterLineFileTarget = 0

			for line in fileOrigin:
				fileTarget.write(line)
				counterLineFileTarget += 1

				if (counterLineFileTarget == 200):
					break

		fileTarget.close
	fileOrigin.close

#EOF