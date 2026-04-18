from socket import *

serveName = '127.0.0.1'
servePort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serveName, servePort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024).decode()
print('From Server: ', modifiedSentence)
clientSocket.close()