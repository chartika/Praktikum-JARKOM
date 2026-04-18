from socket import *

serveName = '127.0.0.1'
servePort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Input lowercase sentence:')

clientSocket.sendto(message.encode(),(serveName,servePort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

clientSocket.close()