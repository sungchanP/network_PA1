from socket import *
from datetime import datetime
import time
import sys

connectionIDList = []

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
     connectionSocket, addr = serverSocket.accept()
     serverSocket.settimeout(120)
     try:
          message = connectionSocket.recv(1024)
          connectionID = message.decode()[-4:]
          if connectionID not in connectionIDList:
               connectionIDList.append(connectionID)
               endTime = time.time() + 30
               if time.time() == endTime:
                    connectionIDList.remove(connectionID)
               response = "OK {} {} {}".format(connectionID, addr[0], addr[1])
               connectionSocket.send(response.encode())
          else:
               response = "RESET {}".format(connectionID)
               connectionSocket.send(response.encode())
          connectionSocket.close()
     except timeout:
          break

serverSocket.close()