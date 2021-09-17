from colorama import Fore, Style
import configparser
from deps.fuzzer import Fuzzing

class Target:
	def __init__(self, args):
		#  URL, File, Save, threads, hidecode, showonly, proxy_country, filterbystring, notshowstring, filterbyregex, notshowregex
		
		self.version = args[0]
		self.URL = args[1]  # URL ( when using --urproxy_country)
		self.phishings_file = args[2]  # URL (when using --file)
		self.save = args[3]  #  output
		self.threads = args[4]  # number of threads
		self.hidecode =  args[5]  # do not show response w/ this http codes
		self.showonly =  args[6]  # show response w/ this http codes
		self.usingProxy= args[7]
		self.search_string =  args[8]
		self.donotsearch_string =  args[9]
		self.regex =  args[10]
		self.dont_regex =  args[11]	
		self.headers = []  # here will be UA loadaded from config
		self.countries = {}  # proxy list {"country":["proxy1"...]}	
		
		if self.phishings_file:  # if user passed a file...
			config = configparser.RawConfigParser()
			config.read(self.phishings_file)
			self.phishing_list = config.items() # load sites from user file, separated by countries ( to use proxy )
			self.urls_object = config  # for fuzzer
		else:
			self.phishing_list = False  # 4 line 71 check

class scanner:
	def __init__(self, *args):
		self.target = Target(args)


	def parse_config(self):
		config = configparser.RawConfigParser()
		try:
			config.read("deps/config.txt")
		except Exception as e:
			print(f"{Fore.RED}Corrupted config file!{Style.RESET_ALL}")
			print(e)
			exit(1)

		self.target.countries = dict(config.items('PROXIES'))  # read proxys from config
		if self.target.usingProxy:
			print(f"\tProxy:\t{Fore.GREEN}{str(self.target.usingProxy)}{Style.RESET_ALL}")

		if self.target.phishing_list:  # prints used proxies when ph file loaded
			print_countries = []
			for i in self.target.phishing_list:
				if i[0] != "DEFAULT":
					print_countries.append(i[0])
			print(f"\tProxy:\t{Fore.GREEN}{str(print_countries)[1:-1]}{Style.RESET_ALL}")	

		if self.target.usingProxy and self.target.usingProxy not in self.target.countries:  # exit if country not in config file
			print(f"\n{Fore.RED}the country is not in the conf file!{Style.RESET_ALL}")
			exit(1)

		if len(self.target.countries):
			for key in self.target.countries:
				self.target.countries[key] = self.target.countries[key].split(',')  # return {"country": ["proxies"]}
		self.target.headers = dict(config.items('HEADERS'))  # read HEADERS from config

	def start(self):
		self.parse_config()

		if self.target.URL:  # do pass  self.headers too!!!
			fuzz = Fuzzing(self.target)
			fuzz.find_shell()

		else:
			fuzz = Fuzzing(self.target)  # constructor overload not allowed in python
			fuzz.find_shell()