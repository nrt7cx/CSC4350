#Nathaniel Tirado
#Client sends four different messages to the server and recieves the corresponding message back.
#Python; socket, argparse, datetime, string, random
#run with command line
from socket import *
import argparse
import datetime as dt
import string
import random

parser = argparse.ArgumentParser()
parser.add_argument("-i","--internet", help="Sets IP Adress for server: ", type=str)
parser.add_argument("-p","--port", help="Sets port Adress for server: ", type=int)
parser.add_argument("-t","--type", help="Sets port Adress for server: ", type=str)
args = parser.parse_args()

serverName = args.internet
serverPort = args.port
internet_Type = args.type
a = False

while(a == False):
    if internet_Type == 'T' or internet_Type == 't':
        clientSocket = socket(AF_INET, SOCK_STREAM)
        num = input("Please enter a value from 1-4: ")
        if num == "1":
                message = "Send IP"
                clientSocket.connect((serverName,serverPort))
                clientSocket.send(message.encode())
                modifiedMessage = clientSocket.recv(1024)
                print (modifiedMessage.decode())
                clientSocket.close
        elif num == "2":
                message = "Send Port"
                clientSocket.connect((serverName,serverPort))
                clientSocket.send(message.encode())
                modifiedMessage = clientSocket.recv(1024)
                print (modifiedMessage.decode())
                clientSocket.close
        elif num == "3":
                currentTime = dt.datetime.now()
                message = "TimeDelay" + str(currentTime)
                clientSocket.connect((serverName,serverPort))
                clientSocket.send(message.encode())
                modifiedMessage = clientSocket.recv(1024)
                timeToSend  = modifiedMessage[0:17].decode()
                currentTime = dt.datetime.now()
                timeNow = modifiedMessage[18:44].decode()
                timeNow = dt.datetime.strptime(timeNow, '%Y-%m-%d %H:%M:%S.%f')
                timeNow = currentTime - timeNow
                print (timeToSend + '|' + str(timeNow))
                clientSocket.close 
        elif num == "4":
                message = "Quit"
                clientSocket.connect((serverName,serverPort))
                clientSocket.send(message.encode())
                modifiedMessage = clientSocket.recv(1024)
                print (modifiedMessage.decode())
                clientSocket.close
                a = True
                
        else: 
                source = string.ascii_lowercase
                randomString = ''.join(random.choice(source)for i in range(8))
                message = randomString
                clientSocket.connect((serverName,serverPort))
                clientSocket.send(message.encode())
                modifiedMessage = clientSocket.recv(1024)
                print(modifiedMessage.decode())
                clientSocket.close
                
        
    if internet_Type == 'U' or internet_Type == 'u':
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        num1 = input("Please enter a value from 1-4: ")
        if num1 == "1":
                message = "Send IP"
                clientSocket.sendto(message.encode(),(serverName,serverPort))
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
                print (modifiedMessage.decode())
                clientSocket.close
        elif num1 == "2":
                message = "Send Port"
                clientSocket.sendto(message.encode(),(serverName,serverPort))
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
                print (modifiedMessage.decode())
                clientSocket.close
        elif num1 == "3":
                currentTime = dt.datetime.now()
                message = "TimeDelay" + str(currentTime)
                clientSocket.sendto(message.encode(),(serverName,serverPort))
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
                timeToSend = modifiedMessage[0:17].decode()
                currentTime = dt.datetime.now()
                timeNow = modifiedMessage[18:44].decode()
                timeNow = dt.datetime.strptime(timeNow, '%Y-%m-%d %H:%M:%S.%f')
                timeNow = currentTime - timeNow
                print (timeToSend + '|' + str(timeNow))
                clientSocket.close 
        elif num1 == "4":
                message = "Quit"
                clientSocket.connect((serverName,serverPort))
                clientSocket.send(message.encode())
                modifiedMessage = clientSocket.recv(1024)
                print (modifiedMessage.decode())
                clientSocket.close
                a = True
        else: 
                source = string.ascii_lowercase
                randomString = ''.join(random.choice(source)for i in range(8))
                message = randomString
                clientSocket.sendto(message.encode(),(serverName,serverPort))
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
                print(modifiedMessage.decode())
                clientSocket.close
       
            
