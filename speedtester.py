#! /home/tasty/speedtester/bin/python

import speedtest
import time
import subprocess

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

try:
	s =  speedtest.Speedtest()
	s.get_servers(servers)
	s.get_best_server()
	s.download(threads=threads)
	s.upload(threads=threads)

	data = s.results.dict()
	
	ping = data['ping']
	upload = data['upload'] /1000000
	download = data['download'] /1000000
	timestamp = time.time()
    
    # Run a command to get the SSID
	ssidcmd = str(subprocess.Popen('iw wlp1s0 info | grep ssid', shell=True, stdout=subprocess.PIPE).stdout.read())
    
    # Extract the SSID by dropping the REGEX characters
	ssid = ssidcmd[9:-3]
    
	total = str(timestamp) + ',' +str(ping) + ',' +str(upload) + ',' + str(download) + ','+ str(ssid) + '\n'

	output = open('output.csv','a')
	output.write(total)
	output.close()

except speedtest.ConfigRetrievalError:

	output = open('output.csv','a')
	
	timestamp = time.time()
	
	total = str(timestamp) + ',' + '0,0,0,0\n'
	
	output.write(total)
	output.close()
