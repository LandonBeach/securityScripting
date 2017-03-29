# A test script for anonBrowser.py
# This test script was taken from the Violent Python book.
# Book written by: T.J. O'Conner
# Author: Landon Beach
# Date: 3/28/17

from anonBrowser import *

# Create a new anonymous browser.
ab = anonBrowser(proxies=[], user_agents=[('User-agent', 'superSecretBrowser')])

# Go to a webpage 4 times, making each visit anonymous.
# For each visit, print the cookies in the cookie jar.
for attempt in range(1,5):
	ab.anonymize()
	print('[*] Fetching page')
	response = ab.open('http://kittenwar.com')
	for cookie in ab.cookie_jar:
		print(cookie)
