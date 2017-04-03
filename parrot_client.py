import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = ("localhost", 4444)
print("Connecting to %s on port %s... " % (svr_addr[0], svr_addr[1]), end='')
sock.connect(svr_addr)
print("Connected!")


try:
	msg = bytes(input("Please enter a message to send: "), "UTF-8")
	sock.sendall(msg)
	data = sock.recv(1024)
	print("Received data: %s" % data.decode())
finally:
	sock.close()
