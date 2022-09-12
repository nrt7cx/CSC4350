from socket import *
import argparse
import time as dt

parser = argparse.ArgumentParser()
parser.add_argument("-t","--type", help="Sets Communitcation Type for server: ", type=str)
parser.add_argument("-p","--port", help="Sets port Adress for server: ", type=int)
args = parser.parse_args()

serverPort = args.port
Type = args.type
print(Type)

if (Type == "U"):
    serverSocket = socket(AF_INET,SOCK_DGRAM) 
    serverSocket.bind(('',serverPort))
    print ("The server is ready to receieve")
    while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	print(message)
        if (message.decode() == "Send IP"):
        	modifiedMessage = clientAddress[0]
        	serverSocket.sendto(modifiedMessage.encode(),clientAddress)
        elif (message.decode() == "Send Port"):
        	modifiedMessage = clientAddress[1]
        	serverSocket.sendto(modifiedMessage.encode(),clientAddress)
elif (Type == "T"):
    serverSocket = socket(AF_INET,SOCK_STREAM) 
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ("The server is ready to receieve")
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        connectionSocket.send(sentence.upper().encode())
        connectionSocket.close()
   
