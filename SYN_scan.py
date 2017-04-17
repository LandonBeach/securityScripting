# This script is a SYN scanner. 
# It takes two arguments: a host, and a list of ports.
# It returns which ports are open or closed.
# Author: Landon Beach
# Date: 4/17/17
import optparse
import threading
from socket import gethostbyname, gethostbyaddr
from scapy.all import *

# This will store the final results of the SYN scan.
results = []

def main():
	''' This function is the main function of the program. 
	It will initiate a SYN scan and then print the results to stdout. 
	'''
	# Add command line options. 
	parser = optparse.OptionParser('usage %prog -H' + ' <target host> -p <target ports>')
	parser.add_option('-H', dest="host", type='string', help='specify target host')
	parser.add_option('-p', dest="ports", type='string', help='specify target ports')

	# Get the arguments from the command line.
	(options, args) = parser.parse_args()
	host = options.host
	ports = options.ports

	# If we don't have any command line arguments, print the usage and exit.
	if host is None or ports is None:
		print(parser.usage)
		exit(0)
	# Else, run the rest of the program
	else:
		try:
			# Get the IP address if the user gives us a domain name.
			ip = socket.gethostbyname(host)
		except:
			# Unknown host, exit with error 1.
			print("[-] Cannot resolve '%s': Unknown host" % host)
			exit(1)
			
		try:
			# Get the domain name if the user gives us an IP address.
			name = socket.gethostbyaddr(ip)
			print("\n[+] Scan Results for: " + name[0])
		except:
			# If we cannot get the name, print out the IP address.
			print("\n[+] Scan Results for: " + ip)
		
		# Scan each port given from the user through the command line with a SYN scan.
		for port in ports.split(','):
			# Create a new thread for a SYN scan.
			t = threading.Thread(target=synScan, args=(host, int(port)))
			
			# Start the thread
			t.start()
			
			# Join the thread. 
			# This will make the main thread wait until all otherthreads are finished.
			t.join()
		
		# SYN scan is finished, sort and print out the results. 
		results.sort()
		for port in results:
			# If the port is open.
			if port[1] == 'open':
				print('  [+] %d/tcp open' % port[0])
				
			# If the port is closed.
			elif port[1] == 'closed':
				print('  [-] %d/tcp closed' % port[0])
			
			# If the port is filtered.
			elif port[1] == 'filtered':
				print('  [+/-] %d/tcp filtered' % port[0])


def synScan(host, port):
	''' This function is a SYN scanner.
	It takes a host and a port and it appends its results to the end of the results list. 
	'''
	# Send a SYN packet to the given host on the given port using a random source port.
	# It returns a tuple, so we split it up between the answered packets and the unanswered packets.
	ans, unans = sr(IP(dst=host) / TCP(sport=RandShort(), dport=port, flags='S'), verbose=False)
	
	# Iterate over each answered packet.
	for pkt in ans:
		# Save the response.
		resp = pkt[1]
		
		# If the response and a TCP layer.
		if resp.haslayer(TCP):
			
			# If the reponse gave us a SYN-ACK (SA) then the port is open.
			# Be nice and send a packet with the RST flag set.
			# This will prevent a SYN flood attack.
			if resp.getlayer(TCP).flags == 0x12:
				results.append([port, 'open'])
				send(IP(dst=host) / TCP(dport=port, flags='R'), verbose=False)
			# If the response gave us a RST then the port is closed.
			elif resp.getlayer(TCP).flags == 0x14:	# RST
				results.append([port, 'closed'])
				
		# If the response has an ICMP layer. The port is probably filtered.
		if resp.haslayer(ICMP):
			if resp.getlayer(ICMP).type == 3 and int(resp.getlayer(ICMP).code in [1,2,3,9,10,13]):
				results.append([port, 'filtered'])

# Run the main function.
if __name__ == "__main__":
	main()
