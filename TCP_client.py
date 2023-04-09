
from socket import *
from datetime import datetime
import sys


clientSocket = socket(AF_INET, SOCK_STREAM)

message = "{} {}".format(sys.argv[1],sys.argv[4])
serverIP = sys.argv[2]
serverPort = int(sys.argv[3])
connectionID = sys.argv[4]

count = 0

try:
    clientSocket.connect((serverIP,serverPort))
    while count < 3:
        clientSocket.send(message.encode())
        clientSocket.settimeout(15)
        try:
            response = clientSocket.recv(1024)
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
                    clientSocket = socket(AF_INET, SOCK_STREAM)
                    clientSocket.connect((serverIP,serverPort))
        except timeout:
            count+=1
            if count < 3:
                print("Connection error {} on {}".format(connectionID, datetime.now()))
                connectionID = input("Please enter a new connection ID: ")
                message = "HELLO {}".format(connectionID)
                clientSocket = socket(AF_INET, SOCK_STREAM)
                clientSocket.connect((serverIP,serverPort))

    print("Connection failure on {}".format(datetime.now()))
    clientSocket.close()

except ConnectionRefusedError:
    print("Connection Failure")
    exit()





# serverName = '127.0.0.1'
# serverPort = 12000
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName,serverPort))
# print("client and server are now connected @ {}".format(datetime.now()))

# sentence = input('Input lowercase sentence: ')
# clientSocket.send(sentence.encode())
# print("<- client sent {} to the server @ {}".format(sentence, datetime.now()))

# modifiedSentence = clientSocket.recv(1024)
# # print ('From Server:', modifiedSentence.decode())
# print("--> client received {} from the server @ {}".format(modifiedSentence.decode(), datetime.now()))

# clientSocket.close()
