from pickle import TRUE
from socket import *
import argparse
import datetime as dt

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
                print (modifiedMessage.decode())
                clientSocket.close 
        elif num == "4":
                a = True
        
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
                print (modifiedMessage.decode())
                clientSocket.close 
        elif num1 == "4":
                a = True
       
        elif internet_Type != 'T' or  internet_Type != 'U' or  internet_Type != 't' or  internet_Type != 'u':
            print("Please input a T or a U.")
            internet_Type = input("Enter T for TCP or U for UDP: ")
