from random import random

output = open('output.csv')
output.close()

for i in range(1, 10):
    for j in range(1,100):
        ping = random()
        upload = random()
        download = random()
        timestamp = random()
        ssid = "ssid" + str(i)

        total = str(timestamp) + ',' + str(ping) + ',' +str(upload) + ',' + str(download) + ','+ str(ssid) + '\n'

        output = open('output.csv', 'a')
        output.write(total)
        output.close()
