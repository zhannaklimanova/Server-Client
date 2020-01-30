import socket
import time
import pickle
import random

# FUNCTIONS

''' sendData(): function to generate random values in the interval [0,256]
	Data will be send to Server.py 
'''
def sendData():
	values = random.randint(0,256)
	return values 

# Creates socket for Client & establishes connection with Server.py at port 3020

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect ((socket.gethostbyname(""), 3020)) 

	# Loop that generated for each piece of data transmitted 

while (1):

	# Sends data to Server.py

	s.send(str(sendData()).encode('utf8'))

	# Receives data from server and displays in console
	
	receivedData = s.recv(3020)
	convertedArray = pickle.loads(receivedData) 
	print(convertedArray)

	time.sleep(2)
s.close



