# import socket and time library
import socket, time

# address and port
HOST = "localhost"
PORT = 20008
buffersize = 1024

x = 0

# socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while loop
while x <= 10:
	# send to server
	x += 1

	MSG = str.encode(str(x))
	sock.sendto(MSG, (HOST, PORT))

	time.sleep(1)

	# recieve
	msg, addr = sock.recvfrom(buffersize)

	print("Msg: ")
	print(msg)
	print(" From: ")
	print(addr)