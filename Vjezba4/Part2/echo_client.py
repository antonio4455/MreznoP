# -- coding: utf-8 --
#echo_client.py
import socket
import datetime 
from local_machine_info import print_machine_info

ime = 'antonio_ribarevic'

print datetime.datetime.now()
print_machine_info()

host=socket.gethostname()
port=12345
client_socket=socket.socket()  
client_socket.connect((host,port))
upit=raw_input('Ispisi text: ')

if(upit == ime):
    print("Taj unos nije podrzan")

client_socket.sendall(upit)
data = client_socket.recv(1024) 

print data 
client_socket.close() 