from socket import *
import argparse
import time as dt



serverPort = 8000

serverSocket = socket(AF_INET,SOCK_DGRAM) 
serverSocket.bind(('',serverPort))
print ("The server is ready to receieve")
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	print(message)
	modifiedMessage = message.decode()
	serverSocket.sendto(modifiedMessage.encode(),clientAddress)

