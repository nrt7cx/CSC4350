from multiprocessing import connection
from operator import mod
from socket import *
import argparse
import datetime as dt


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
        
        if(message.decode() == "Send IP"):
            modifiedMessage = clientAddress[0]
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
        elif(message.decode() == "Send Port"):
            modifiedMessage = str(clientAddress[1])
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
        elif(message.decode()[0:9] == "TimeDelay"):
            timeDelay = dt.datetime.strptime(message.decode()[9:35], '%Y-%m-%d %H:%M:%S.%f')
            timeNow = dt.datetime.now()
            print(timeDelay)
            print(timeNow)
            timeNow = timeNow - timeDelay
            modifiedMessage = str(timeNow) + str(dt.datetime.now())
            print(timeNow)
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)


    
if (Type == "T"):
    serverSocket = socket(AF_INET,SOCK_STREAM) 
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ("The server is ready to receieve")
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        print(sentence)
        Time = "TimeDelay2022-09-12 15:35:05.865171"
        if (sentence == "Send IP"):
            connectionSocket.send(addr[0].encode())
            connectionSocket.close()
        elif (sentence == "Send Port"):
            connectionSocket.send(str(addr[1]).encode())
            connectionSocket.close()
        elif(sentence[0:9] == "TimeDelay"):
            connectionSocket.send(sentence[9:35].encode())
            connectionSocket.close()

