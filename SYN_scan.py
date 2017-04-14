import optparse
import threading
from socket import gethostbyname, gethostbyaddr
from scapy.all import *

results = []

def main():
	parser = optparse.OptionParser('usage %prog -H' + ' <target host> -p <target ports>')
	parser.add_option('-H', dest="host", type='string', help='specify target host')
	parser.add_option('-p', dest="ports", type='string', help='specify target ports')

	(options, args) = parser.parse_args()
	host = options.host
	ports = options.ports

	if host is None or ports is None:
		print(parser.usage)
		exit(0)
	else:
		try:
			ip = socket.gethostbyname(host)
		except:
			print("[-] Cannot resolve '%s': Unknown host" % host)
			exit(1)
			
		try:
			name = socket.gethostbyaddr(tgtIP)
			print("\n[+] Scan Results for: " + name[0])
		except:
			print("\n[+] Scan Results for: " + ip)
		
		for port in ports.split(','):
			t = threading.Thread(target=synScan, args=(host, int(port)))
			t.start()
			t.join()
		
		results.sort()
		for port in results:
			if port[1] == 'open':
				print('  [+] %d/tcp open' % port[0])
			elif port[1] == 'closed':
				print('  [-] %d/tcp closed' % port[0])
			elif port[1] == 'filtered':
				print('  [+/-] %d/tcp filtered' % port[0])
	

def synScan(host, port):
	ans, unans = sr(IP(dst=host) / TCP(sport=RandShort(), dport=port, flags='S'), verbose=False)
	for pkt in ans:
		resp = pkt[1]
		if resp.haslayer(TCP):
			if resp.getlayer(TCP).flags == 0x12:	# SA
				results.append([port, 'open'])
				send(IP(dst=host) / TCP(dport=port, flags='R'), verbose=False)
			elif resp.getlayer(TCP).flags == 0x14:	# RST
				results.append([port, 'closed'])
		if resp.haslayer(ICMP):
			if resp.getlayer(ICMP).type == 3 and int(resp.getlayer(ICMP).code in [1,2,3,9,10,13]):
				results.append([port, 'filtered'])
			
if __name__ == "__main__":
	main()
