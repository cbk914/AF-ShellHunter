import configparser
# import threading

class Fuzzing:

	def __init__(self,URL, search_string, notsearch_string, regex, dont_regex, hidecode, showonly, usingProxy, save_here):
		self.URL = URL  # URL to scan
		self.search_string = search_string  # False or string to grep
		self.notsearch_string = notsearch_string  # False or string to inverse grep
		self.regex = regex  # False or regex to grep
		self.dont_regex = dont_regex # False or regex to inverse grep
		self.hidecode = hidecode # do not show this codes
		self.showonly = showonly  # show only http status code
		self.usingProxy = usingProxy  # False or COUNTRY to use, NOT proxy
		self.save = save_here
	def __init__(self, config_object, save_here):  # overload, if using config object ( loaded phishing list )
		self.save = save_here
		self.scan_config_list = config_object
		# asign all variables as normal


	def find_shell(self): # just search
		for i in self.scan_config_list.items():
			print(i)
	#def __init__(self):
	#	pass
