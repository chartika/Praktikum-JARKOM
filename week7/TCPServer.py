from socket import *

servePort = 12000
serveSocket = socket(AF_INET,SOCK_STREAM)

serveSocket.bind(('', servePort))
serveSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serveSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()