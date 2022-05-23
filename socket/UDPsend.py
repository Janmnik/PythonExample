import socket

UDP_IP = "localhost"
UDP_PORT = 50001
message = b"Hello User!"

print(f"UDP target IP: {UDP_IP}")
print(f"UDP target port: {UDP_PORT}")
print(f"message: {message}")

print("press ctrl + c to close program")
print("Gve me a message:")
message = bytes(input("> "), 'utf-8')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Internet, Udp
sock.sendto(message, (UDP_IP, UDP_PORT))


data, addr = sock.recvfrom(1024) #buffer size is 1024 bytes
sock.settimeout(1) #timeout
data = data.upper() #response

sock.settimeout(2)
print("from: ", addr)

if data[0] == 65 and data[1] == 67 and data[2] == 75 and data[3] == 33:
    print("response message:", data)
else:
    sock.close()


