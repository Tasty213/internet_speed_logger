#! /home/tasty/speedtester/bin/python

import speedtest
import time
import subprocess
import schedule
import sys

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

arguments = len(sys.argv)

verbose = False

for i in range(1, arguments):
    current = sys.argv[i]
    if current == "-v" or current == "--verbose":
        verbose = True

def perform_test(verbose=False):
    verbose = True
    if verbose:
        print("Running test function")
    try:
        s =  speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        if verbose:
            print("connection established, performing test")
        s.download(threads=threads)
        s.upload(threads=threads)

        if verbose:
            print("test complete")

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

        if verbose:
            print("saving: ", total)

        output = open('output.csv','a')
        output.write(total)
        output.close()

    except speedtest.ConfigRetrievalError:


        timestamp = time.time()

        total = str(timestamp) + ',' + '0,0,0,0\n'

        if verbose:
            print("failed to connect")
            print("saving: ", total)

        output = open('output.csv','a')
        output.write(total)
        output.close()

    if verbose:
        print("finished test")


if verbose:
    print("adding schedule task")

schedule.every(10).seconds.do(perform_test, verbose = True)

while True:
    schedule.run_pending()
    if verbose:
        print("sleeping")
    time.sleep(1)
