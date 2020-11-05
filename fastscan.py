import multiprocessing
import subprocess
import os
from datetime import datetime

def pinger( jobQueue, resultsQueue ):
	DEVNULL = open(os.devnull,"w")
	while True:
		ip = jobQueue.get()
		if ip is None: break

		try:
			subprocess.check_call(['ping', '-c1',ip], stdout=DEVNULL)
			resultsQueue.put(ip)
		except:
			pass

if __name__ == "__main__":
	net = input("Enter the Network Address: ")
	netTemp = net.split(".")
	netBits = netTemp[0] + "." + netTemp[1] + "." + netTemp[2] + "."
	startTime = datetime.now()
	print("Commencing Scan...")

	poolSize = 255

	jobs = multiprocessing.Queue()
	results = multiprocessing.Queue()

	pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
		for i in range(poolSize) ]

	for p in pool:
		p.start()

	for i in range(1,255):
		jobs.put(netBits + str(i))

	for p in pool:
		jobs.put(None)

	for p in pool:
		p.join()

	while not results.empty():
		ip = results.get()
		print("Host at: " + ip + " detected on the network")

print ("Scan completed in: " + str(datetime.now() - startTime) + " seconds")




