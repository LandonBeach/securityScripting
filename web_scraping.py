# This is an Anonymous Browser taken out of the Violent Python Book
# Book written by: T.J. O'Conner
# Author: Landon Beach
# Date: 4/20/17
from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os
import optparse
import re

def printLinks(url):
	''' This function will find and print all of the links on a website 
	from a URL. It will try to print them using Regex first and then it 
	will try to print them using BeautifulSoup. 
	'''
	# Create an anonymous browser
	ab = anonBrowser()
	ab.anonymize()
	
	# Open the URL in the anonymous browser.
	page = ab.open(url)
	
	# Get the HTML from the web page.
	html = page.read()
	
	# Try to print all of the links using Regex.
	try:
		print("[+] Printing Links From Regex.")
		link_finder = re.compile('href="(.*?)"')
		links = link_finder.findall(html)
		
		# Print all of the found links.
		for link in links:
			print(link)
	# Catch any exceptions, but do nothing with it.
	except:
		pass
		
	# Try to print all of the links using BeautifulSoup.
	try:
		print("\n[+] Printing Links From BeautifulSoup.")
		soup = BeautifulSoup(html)
		links = soup.findall(name='a')
		
		# Print all of the found links.
		for link in links:
			# If it has 'href' then it is a link, so print the link.
			if link.has_key('href'):
				print(link['href'])
	# Catch any exceptions, but do nothing with it.
	except:
		pass
		
def main():
	''' This is the main function. It takes an argument from the command 
	line and it will print all of the links on a website from a given URL.
	'''
	# Create command line arguments.
	parser = optparse.OptionParser('useage %prog -u <target URL>')
	parser.add_option('-u', dest='url', type='string', help='specify target URL')
	
	# Get the command line arguments.
	(options, args) = parser.parse_args()
	url = options.url
	
	# If we don't have a URL from the command line, then print the usage and exit.
	if url is None:
		print(parser.usage)
		exit(0)
	# Print all of the links from the given URL.
	else:
		printLinks(url)

# Run the main function if module isn't being imported.
if __name__ == '__main__':
	main()
