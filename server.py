# import socket and time library
import socket, time

# address and port
HOST = "localhost"
PORT = 20008
buffersize = 1024

x = 10

# socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

# while loop
while x >= 0:
	x -= 1
	# recieve
	msg, addr = sock.recvfrom(buffersize)

	print("Msg: ")
	print(msg)
	print(" From: ")
	print(addr)

	time.sleep(1)

	# send
	MSG = str.encode(str(x))
	sock.sendto(MSG, addr)