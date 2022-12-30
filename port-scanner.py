# Port Scanner made in Python

import socket
import subprocess
import sys

from datetime import datetime

# Blank screen
subprocess.call('clear', shell=True)

# Ask for input
remoteHost = raw_input("Enter a remote host to scan: ")
remoteHost_IP = socket.gethostbyname(remoteHost)

# Print a nice banner with information on which host we are about to scan
print "_" * 60
print "Please wait, scanning remote host", remoteHost_IP
print "_" *60

# Check the date and time the scan was started
timing1 = datetime.now()

# Using the range function to specify ports and error handling

try:
for port in range (1,5000):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((remoteHost_IP, port))
if result ==0:
print "Port {}:        Open".format(port)
sock.close()

except KeyboardInterrupt:
print "You pressed Ctrl+C, canceling the operation"
sys.exit()

except socket.gaierror:
print "Hostname could not be resolved. Exiting"
sys.exit()

except socket.error:
print "Couldn't connect to server"
sys.exit()

# Checking time again
timing2 = datetime.now()

# Calculate the difference in time to now how long the scan took
total = timing2 - timing1

# Printing the information on the screen
print 'Scanning Completed in: ', total
