# This is a server that sends back the data that it receives.
# Author: Landon Beach
# Date: 4/5/17

import socket, argparse

# Parse the arguments and assign it to the variable "options".
parser = argparse.OptionParser()
parser.add_argument("-s", "--server", default="127.0.0.1", dest="svr_addr", help="Bind to IP address SERVER_IP", metavar="SERVER_IP")
parser.add_argument("-p", "--port", default=4444, type="int", dest="svr_port", help="Bind to port SERVER_PORT", metavar="SERVER_PORT")
(options, args) = parser.parse_args()

# Create a socket using the arguments given.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = (options.svr_addr, options.svr_port)

try:
	# Bind to the socket and start a listener.
	sock.bind(svr_addr)
	sock.listen(1)
	print("Listening on %s on port %d." % (svr_addr[0], svr_addr[1]))
	
	# Wait for a connection to the socket listener.
	connection, client_addr = sock.accept()
	print("Connection from %s" % client_addr[0])

	while True:
		# Receive data from the connected client.
		raw_data = connection.recv(1024)
		
		# If there is data, print it and send it back to the client.
		if raw_data:
			data = raw_data.decode()
			print("[Received message from %s] %s" % (client_addr[0], data))
			connection.sendall(raw_data)
			print("[Sent message to %s] %s" % (client_addr[0], data))
		else:
			break
	
finally:
	# Close the connection to the client.
	connection.close()
