#Nathaniel Tirado
#Server recieves four different messages from the client and sends the corresponding message back.
#Python; socket, argparse, datetime, logging
#run with command line
from socket import *
import argparse
import datetime as dt
import logging

parser = argparse.ArgumentParser()
parser.add_argument("-t","--type", help="Sets Communitcation Type for server: ", type=str)
parser.add_argument("-p","--port", help="Sets port Adress for server: ", type=int)
args = parser.parse_args()

serverPort = args.port
Type = args.type
print(Type)

if (Type == "U" or Type == "u"):
    serverSocket = socket(AF_INET,SOCK_DGRAM) 
    serverSocket.bind(('',serverPort))
    print ("The server is ready to receieve")
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(message)
        logging.basicConfig(filename='protocols.txt', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        if(message.decode() == "Send IP"):
            modifiedMessage = "OK: " + clientAddress[0]
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            logging.info('| IP |' + ' VALID')
        elif(message.decode() == "Send Port"):
            modifiedMessage = "OK: " + str(clientAddress[1])
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            logging.info('| PORT |' + ' VALID')
        elif(message.decode()[0:9] == "TimeDelay"):
            timeDelay = dt.datetime.strptime(message.decode()[9:35], '%Y-%m-%d %H:%M:%S.%f')
            timeNow = dt.datetime.now()
            print(timeDelay)
            print(timeNow)
            timeNow = timeNow - timeDelay
            modifiedMessage = "OK: " + str(timeNow) + str(dt.datetime.now())
            print(modifiedMessage)
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            logging.info('| TIMEDELAY |' + ' VALID')
        elif(message.decode() == "Quit"):
            modifiedMessage = "OK: Quit Program"
            print(modifiedMessage)
            logging.info('| QUIT |' + ' VALID')
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)

        else: 
            logging.warning('| NULL |' + ' INVALID')
            modifiedMessage = "INVALID"
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            

    
elif (Type == "T" or Type == "t"):
    serverSocket = socket(AF_INET,SOCK_STREAM) 
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ("The server is ready to receieve")
    while True:
        logging.basicConfig(filename='protocols.txt', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        print(sentence)
        if (sentence == "Send IP"):
            modifiedSentence = "OK: " + addr[0]
            connectionSocket.send(modifiedSentence.encode())
            connectionSocket.close()
            logging.info('| IP |' + ' VALID')
        elif (sentence == "Send Port"):
            modifiedSentence = "OK: " + str(addr[1])
            connectionSocket.send(modifiedSentence.encode())
            connectionSocket.close()
            logging.info('| PORT |' + ' VALID')
        elif(sentence[0:9] == "TimeDelay"):
            timeDelay = dt.datetime.strptime(sentence[9:35], '%Y-%m-%d %H:%M:%S.%f')
            timeNow = dt.datetime.now()
            print(timeDelay)
            print(timeNow)
            timeNow = timeNow - timeDelay
            modifiedSentence = "OK: " + str(timeNow) + str(dt.datetime.now())
            print(timeNow)
            connectionSocket.send(modifiedSentence.encode())
            connectionSocket.close()
            logging.info('| TIMEDELAY |' + ' VALID')
        elif(sentence == "Quit"):
            modifiedSentence = "OK: Quit Program"
            print(modifiedSentence)
            logging.info('| QUIT |' + ' VALID')
            connectionSocket.send(modifiedSentence.encode())
            connectionSocket.close()

        else: 
            logging.warning('| NULL |' + ' INVALID')
            modifiedSentence = "INVALID"
            connectionSocket.send(modifiedSentence.encode())    
else: #not entirely sure if this is useless code
    print("Please enter a T or a U.") 