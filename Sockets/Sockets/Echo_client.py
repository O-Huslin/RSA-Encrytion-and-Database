#Echo client program
# From https://docs.python.org/3/library/socket.html

import socket

HOST = 'localhost'	# The remote host
PORT = 50007	# Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
sentence = input('Enter string to echo:')
data = str.encode(sentence)
s.sendall(data)
echoedData = s.recv(1024)
s.close()
print('Received: ', bytes.decode(echoedData))
