import subprocess
import os
from datetime import datetime

net = input ("Enter the Network Address: ")
netTemp = net.split(".")
netBits = netTemp[0] + "." + netTemp[1] + "." + netTemp[2] + "."
alive = []
startTime = datetime.now()

print ("Scanning in Progress:")

for ip in range(1,255):
	host = netBits + str(ip)
	isAlive  = subprocess.call(['ping', '-c1', host])
	if isAlive == 0:
		alive.append("Host at: " + host + " detected on the network")

for i in alive:
	print(i)

print ("Scan completed in: " + str(datetime.now() - startTime) + " seconds")
