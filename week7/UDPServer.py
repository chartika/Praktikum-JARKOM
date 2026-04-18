from socket import *

servePort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.bind(('', servePort))
print('The server is ready to receive')

while True:
    message, clientAddress = clientSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    clientSocket.sendto(modifiedMessage.encode(), clientAddress)