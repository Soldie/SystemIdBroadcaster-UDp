#!/usr/bin/python

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nikeah
#
# Created:     19/11/2017
# Copyright:   (c) Nikeah 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import threading
import receiver
import sender
import time

from ConfigurationManager.ConfigurationManager import ConfigurationManager

def main():
	fileManager = ConfigurationManager('broadcast.config')
	configurationData = fileManager.GetConfigurationData()
	
	#print configurationData.GetPort()
	#print configurationData.GetMessage()
	
	port = configurationData.GetPort()

	t = threading.Thread(target=receiver.StartListener, args=[port])
	t.start()

	time.sleep(2)

	sender.TransmitData(port)

if __name__ == '__main__':
	main()
