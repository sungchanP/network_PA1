from socket import *
from datetime import datetime
import sys


clientSocket = socket(AF_INET, SOCK_DGRAM)

message = "{} {}".format(sys.argv[1],sys.argv[4])
serverIP = sys.argv[2]
serverPort = int(sys.argv[3])
connectionID = sys.argv[4]

count = 0

while count < 3:
    clientSocket.sendto(message.encode(), (serverIP, serverPort))
    clientSocket.settimeout(15)
    try:
        response, serverAddress = clientSocket.recvfrom(2048)
        responseArr = response.decode().split(' ')
        if responseArr[0] == "OK":
            print("Connection established {} {} {} on {}".format(connectionID, responseArr[2], responseArr[3], datetime.now()))
            clientSocket.close()
            exit()
        else:
            count+=1
            if count < 3:
                print("Connection error {} on {}".format(connectionID, datetime.now()))
                connectionID = input("Please enter a new connection ID: ")
                message = "HELLO {}".format(connectionID)
    except timeout or ConnectionResetError:
        count+=1
        if count < 3:
            print("Connection error {} on {}".format(connectionID, datetime.now()))
            connectionID = input("Please enter a new connection ID: ")
            message = "HELLO {}".format(connectionID)

print("Connection failure on {}".format(datetime.now()))
clientSocket.close()
