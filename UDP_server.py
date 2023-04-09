from socket import *
from datetime import datetime
import time
import sys

connectionIDList = []

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

while True:
    message, clientAddress = serverSocket.recvfrom(2048) 
    connectionID = message.decode()[-4:]
    serverSocket.settimeout(120)
    try:
        if connectionID not in connectionIDList:
            connectionIDList.append(connectionID)
            endTime = time.time() + 30
            if time.time() == endTime:
                connectionIDList.remove(connectionID)
            response = "OK {} {} {}".format(connectionID, clientAddress[0], clientAddress[1])
            serverSocket.sendto(response.encode(), clientAddress)
        else:
            response = "RESET {}".format(connectionID)
            serverSocket.sendto(response.encode(), clientAddress)
    except timeout:
        break

serverSocket.close()
