import socket

client_socket = socket.socket()
host = socket.gethostbyname('www.google.com')
port = 80

client_socket.connect((host,port))
print ('The socket has successfully connected to Google on port', port, 'And IP address', host)

client_socket.close()
