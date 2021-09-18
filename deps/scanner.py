from colorama import Fore, Style
import configparser
from deps.fuzzer import Fuzzing

class Target:  # where current URL and its options are stored ( if -u class do not change; else deps.fuzzer.parser_options_config_file will change 4 each URL in urls_file)
	def __init__(self, args):
		#  URL, File, Save, threads, hidecode, showonly, proxy_country, filterbystring, notshowstring, filterbyregex, notshowregex
		
		self.version = args[0]
		self.URL = args[1]  # URL ( when using --url )
		self.phishings_file = args[2]  # phishing file (when using --file)
		self.save = args[3]  #  save output here
		self.threads = args[4]  # number of threads to run, default is 20
		self.hidecode =  args[5]  # do not show response w/ this http codes
		self.showonly =  args[6]  # show response w/ this http codes
		self.usingProxy= args[7]  # current proxy to use
		self.search_string =  args[8]
		self.donotsearch_string =  args[9]
		self.regex =  args[10]
		self.dont_regex =  args[11]	
		self.headers = {}  # here will be UA loadaded from config
		self.countries = {}  # proxy list {"country":["proxy1"...]}	
		self.phishing_list = []  # URL file loaded 
		self.shellfile = args[12]

class scanner:
	def __init__(self, *args):
		self.target = Target(args)


	def parse_config(self):
		config = configparser.RawConfigParser()
		try:
			config.read("user_files/config.txt")
		except Exception as e:
			print(f"{Fore.RED}Corrupted config file!{Style.RESET_ALL}")
			print(e)
			exit(1)
		self.target.countries = dict(config.items('PROXIES'))  # read proxys from config and save to using proxy countries

		if self.target.usingProxy and self.target.usingProxy not in self.target.countries:  # exit if country not in config file
			print(f"\n{Fore.RED}the country is not in the conf file!{Style.RESET_ALL}")
			exit(1)


		if len(self.target.countries):
			for key in self.target.countries:
				self.target.countries[key] = self.target.countries[key].split(',')  # return {"country": ["proxies"]}
		self.target.headers = dict(config.items('HEADERS'))  # read HEADERS from config

	def start(self):
		self.parse_config()
		fuzz = Fuzzing(self.target)
		fuzz.start_fuzz()