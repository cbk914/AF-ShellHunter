from colorama import Fore, Style
import configparser

class scanner:
	def __init__(self,version, URL, File, Save, threads, hidecode, showonly, proxy_country, filterbystring, notshowstring, filterbyregex, notshowregex):

		self.URL = URL  # URL ( when using --urproxy_country)
		self.usingProxy=proxy_country
		self.phishings_file = File  # URL (when using --file)
		self.save = Save  #  output
		self.threads = threads  # number of threads
		self.headers = []  # here will be UA loadaded from config
		self.countries = {}  # proxy list {"country":["proxy1"...]}
		self.hidecode = hidecode  # do not show response w/ this http codes
		self.showonly = showonly  # show response w/ this http codes
		self.version = version
		self.search_string = filterbystring
		self.donotsearch_string = notshowstring
		self.regex = filterbyregex
		self.dont_regex = notshowregex
		if File:
			config = configparser.RawConfigParser()
			try:
				config.read(File)
			except Exception as e:
				print(f"{Fore.RED}Corrupted phishing file!{Style.RESET_ALL}")
				print(e)
				exit(1)
			self.phishing_list = config.items() # load sites from user file, separated by countries ( to use proxy )

	def banner(self):
		print(f"{Fore.GREEN}Running AF-Team ShellHunt {self.version}{Style.RESET_ALL}")
		if self.phishings_file:
			print(f"\tURLs File:\t{Fore.GREEN}{self.phishings_file}{Style.RESET_ALL}")
		else:
			print(f"\tURL:\t{Fore.GREEN}{self.URL}{Style.RESET_ALL}")

		if self.save:
			print(f"\tSaving to:\t{Fore.GREEN}{self.save}{Style.RESET_ALL}")

		if self.hidecode:
			print(f"\tNot showing\t{Fore.RED}{str(self.hidecode)[1:-1]}{Style.RESET_ALL}")
		if self.showonly:
			print(f"\tShowing only\t{Fore.GREEN}{str(self.showonly)[1:-1] }{Style.RESET_ALL}")
		print(f"\tThreads:\t{Fore.GREEN}{self.threads}{Style.RESET_ALL}")

		if self.search_string:
			print(f"\tShowing only coincidence with:\t{Fore.GREEN}{self.search_string}{Style.RESET_ALL}")
		if self.donotsearch_string:
			print(f"\tNot showing coincidence with:\t{Fore.RED}{self.donotsearch_string}{Style.RESET_ALL}")
		if self.regex:
			print(f"\tShowing only coincidence with:\t{Fore.GREEN}{self.regex}{Style.RESET_ALL}")
		if self.dont_regex:
			print(f"\tNot showing coincidence with:\t{Fore.RED}{self.dont_regex}{Style.RESET_ALL}")

	def parse_config(self):
		config = configparser.RawConfigParser()
		try:
			config.read("deps/config.txt")
		except Exception as e:
			print(f"{Fore.RED}Corrupted config file!{Style.RESET_ALL}")
			print(e)
			exit(1)

		self.countries = dict(config.items('PROXIES'))  # read proxys from config
		if self.usingProxy:
			print(f"\tProxy:\t{Fore.GREEN}{str(self.usingProxy)}{Style.RESET_ALL}")

		if self.phishing_list:
			print_countries = []
			for i in self.phishing_list:
				if i[0] != "DEFAULT":
					print_countries.append(i[0])
			print(f"\tProxy:\t{Fore.GREEN}{str(print_countries)[1:-1]}{Style.RESET_ALL}")	

		if self.usingProxy and self.usingProxy not in self.countries:  # exit if country not in config file
			print(f"{Fore.RED}the country is not in the conf file!{Style.RESET_ALL}")
			exit(1)

		if len(self.countries):
			for key in self.countries:
				self.countries[key] = self.countries[key].split(',')  # return {"country": ["proxies"]}
		self.headers = dict(config.items('HEADERS'))  # read HEADERS from config


				# random.choice(self.countries[country])
	"""
	def beautifyURL(self, fcn):
		def inner(urls):
			if not url.startswith("http")
				"http://"+=url
			if not url.endswith("/"):
				url+="/"
		return inner
		""" 

	def find(self, url):
		pass

	def start(self):
		self.banner()
		self.parse_config()

		if self.URL:
			#@beautifyURL
			self.find(self.URL)
		else:
			pass # multiple UIRLSa



			# for each url print using proxy and filters