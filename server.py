from http import server
from multiprocessing import connection
from socket import *
import argparse
from sqlite3 import connect
import time as dt

parser = argparse.ArgumentParser()
parser.add_argument("-t","--type", help="Sets Communitcation Type for server: ", type=str)
parser.add_argument("-p","--port", help="Sets port Adress for server: ", type=int)
args = parser.parse_args()

serverPort = args.port
Type = args.type

if (Type == "U"):
    serverSocket = socket(AF_INET,SOCK_DGRAM) 
    serverSocket.bind(('',serverPort))
    print ("The server is ready to receieve")
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(message)
        modifiedMessage = message.decode()
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
   
