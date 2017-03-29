# This is an Anonymous Browser taken out of the Violent Python Book
# Book written by: T.J. O'Conner
# Author: Landon Beach
# Date: 3/28/17

import mechanize, cookielib, random

class anonBrowser(mechanize.Browser):
	""" This class is an Anonymous Browser """
	def __init__(self, proxies=[], user_agents=[]):
		""" A constructor that initializes the Anonymous Browser.
		This method takes a list of proxys that the browser can use and
		it takes a list of User Agent strings.
		"""
		# Initalize a new browser.
		mechanize.Browser.__init__(self)
		self.set_handle_robots(False)
		
		# Set the proxies and User Agent strings.
		self.proxies = proxies
		self.user_agents = user_agents + ['Mozilla/4.0', \
			'FireFox/6.01', 'ExactSearch', 'Nokia7110/1.0']
		
		# Set a new cookie jar and make the browser anonymous.
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
		self.anonymize()

	def clear_cookies(self):
		""" This method clears all of the cookies in the cookie jar. """
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)

	def change_user_agent(self):
		""" This method will change to a random User Agent. """
		index = random.randrange(0, len(self.user_agents))
		self.addheaders = [('User-agent', \
			(self.user_agents[index]))]

	def change_proxy(self):
		""" This method will change to a random proxy. """
		if self.proxies:
			index = random.randrange(0, len(self.proxies))
			self.set_proxies({'http': self.proxies[index]})

	def anonymize(self, sleep=False):
		""" This method will make the browser anonymous by clearing the 
		cookies in the cookie jar, changing to a random User Agent, and
		changing to a random proxy. If the sleep parameter is set to
		true, then it will sleep for 60 seconds.
		"""
		self.clear_cookies()
		self.change_user_agent()
		self.change_proxy()
		if sleep:
			time.sleep(60)
