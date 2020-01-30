import socket
import random 
import time
import pickle
import os 
from datetime import datetime
import time 


# VARIABLES

''' newFile: Creates a txt file in the Server.py/Client.py path directory 
 	(best to create in desktop, same location as Server/Client; easier to access)
'''

newFile = open("PlottedData.txt", 'w', buffering=1)



# initialTime: Calculates time at the start of runtime in seconds

initialTime =  round((datetime.today()).timestamp())



#FUNCTIONS 

# timeDifference(): function to compute the time difference between each data that is incoming

def timeDifference(): 
	time2SecondsAfter = (round((datetime.today()).timestamp()))
	global initialTime 
	timeDifference = time2SecondsAfter - initialTime
	return (timeDifference - 1)



''' sendData(): function to generate random values in the interval [0,5]
	Data will be send to Client.py 
'''
def sendData():
	values = random.randint(0,5)
	return values 



''' myServer(): main function that creates socket, sends data to Client.py, 
	receives data from Client.py, creates PlottedData.txt file, 
	writes to PlottedData.txgt
''' 	
def myServer(): 
		# Creates socket for Server & waits for connection

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Server Started waiting for client connection")

		# Creates server at socket.gethostname() port 3020 & establishes connection

	s.bind((socket.gethostbyname(""), 3020)) 
	s.listen(5)
	connection, address = s.accept() 
	print(f"Connection to {address} established!")

		# Loop that generated for each piece of data transmitted 

	while (True): 
		dataReceived = int(connection.recv(3020).decode('utf8'))
		if not dataReceived: 
			break
		print("Data received from client: " + str(dataReceived))

		# Writes received data to file PlottedData.py created previously 
		newFile.write(str(timeDifference()) + "," + str(dataReceived) + "\n")
		newFile.flush()

		# Sends data to client as an array of size 4
		arraySentToServer = [sendData() for x in range(4)]
		data_string = pickle.dumps(arraySentToServer)
		connection.send(data_string)


		# Interval at which data is received, displayed, sent
		time.sleep(2)

		# Exit command. Can be commented out for the 
		# program to continue indefinitly
		
		if (int(timeDifference()) > 60):
			sys.exit()
    

myServer() 
