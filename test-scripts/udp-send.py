import socket
import sys
import time
# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# Let's send data through UDP protocol
for i in range(1000):
	send_data = 'LIST'
	send = b'\x77\x02\x00' #\x00\xC2\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
	#print(send, len(send))
	s.sendto(send, ('127.0.0.1', 8000))
	#data, address = s.recvfrom(4096)
	#print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
	#print("\n\n 1. Client Sent : ", send_data, "\n\n")
	print(i, list(send))
# close the socket
s.close()