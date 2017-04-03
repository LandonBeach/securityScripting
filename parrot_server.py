import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = ("localhost", 4444)

try:
	sock.bind(svr_addr)
	sock.listen(1)
	print("Listening on %s on port %d." % (svr_addr[0], svr_addr[1]))
	
	connection, client_addr = sock.accept()
	print("Connection from %s" % client_addr[0])

	while True:
		raw_data = connection.recv(1024)
		if raw_data:
			data = raw_data.decode()
			print("[Received message from %s] %s" % (client_addr[0], data))
			connection.sendall(raw_data)
			print("[Sent message to %s] %s" % (client_addr[0], data))
		else:
			break
	
finally:
	connection.close()
