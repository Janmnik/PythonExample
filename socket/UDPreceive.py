import socket
import random

message = b"ACK! "

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("press ctrl + c to close program")
print("Gve me a port:")
port = input("> ")
if port=="":
    sock.bind(('', 50000))
else:
    sock.bind(('', int(port)))

print(sock)
print("-------------------")
print("~Receiver~")


while True:
    rand = random.randint(0, 10)
    data, addr = sock.recvfrom(1024) #buffer size is 1024 bytes
    data = data.upper()
    print("from: ", addr)    
    print("received message:", data)
    if data != "":
        sock.sendto(message+bytes(rand), addr)
