# This is a simple client that sends a message to a server.
# Author: Landon Beach
# Date: 4/5/17
import socket, argparse

# Parse the arguments and assign it to the variable "options".
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", default="127.0.0.1", dest="svr_addr", help="Connect to IP address SERVER_IP", metavar="SERVER_IP")
parser.add_argument("-p", "--port", default=4444, type="int", dest="svr_port", help="Connect to port SERVER_PORT", metavar="SERVER_PORT")
parser.add_argument("-m", "--message", default=" ", dest="message", help="Send MESSAGE to server", metavar="MESSAGE")
(options, args) = parser.parse_args()

# Connect to the server IP and port given from the arguments.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = (options.svr_addr, options.svr_port)
print("Connecting to %s on port %s... " % (svr_addr[0], svr_addr[1]), end='')
sock.connect(svr_addr)
print("Connected!")


try:
	# Send the message from the arguments to the server.
	msg = bytes(options.message, "UTF-8")
	sock.sendall(msg)
	
	# Receive and print the data from the server.
	data = sock.recv(1024)
	print("Received data: %s" % data.decode())
	
finally:
	# Close the socket to the server.
	sock.close()
