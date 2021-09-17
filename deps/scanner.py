from colorama import Fore, Style
import configparser
from deps.fuzzer import Fuzzing

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
		if File:  # if user passed a file...
			config = configparser.RawConfigParser()
			config.read(File)
			self.phishing_list = config.items() # load sites from user file, separated by countries ( to use proxy )
			self.urls_object = config  # for fuzzer
		else:
			self.phishing_list = False  # 4 line 71 check


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

		if self.phishing_list:  # prints used proxies when ph file loaded
			print_countries = []
			for i in self.phishing_list:
				if i[0] != "DEFAULT":
					print_countries.append(i[0])
			print(f"\tProxy:\t{Fore.GREEN}{str(print_countries)[1:-1]}{Style.RESET_ALL}")	

		if self.usingProxy and self.usingProxy not in self.countries:  # exit if country not in config file
			print(f"\n{Fore.RED}the country is not in the conf file!{Style.RESET_ALL}")
			exit(1)

		if len(self.countries):
			for key in self.countries:
				self.countries[key] = self.countries[key].split(',')  # return {"country": ["proxies"]}
		self.headers = dict(config.items('HEADERS'))  # read HEADERS from config

	def start(self):
		self.parse_config()

		if self.URL:  # do pass  self.headers too!!!
			fuzz = Fuzzing(self.URL, self.search_string, self.donotsearch_string, self.regex, self.dont_regex, self.hidecode, self.showonly, self.usingProxy, self.save, self.version, self.threads)
			fuzz.find_shell()
			"""
			overload -> url to scan, show match, do not show match, show regex match, do not show regex match, do not show results w/ status code, show only w/ this codes, proxy country
			 """
		else:
			fuzz = Fuzzing(self.urls_object, self.save, self.version)  # constructor overload not allowed in python
			fuzz.find_shell()