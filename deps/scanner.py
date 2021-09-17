from colorama import Fore, Style
import configparser

class scanner:
	def __init__(self,version, URL, File, Save, threads, hidecode, showonly):
		self.URL = URL  # URL ( when using --url)
		self.phishings_file = File  # URL (when using --file)
		self.save = Save  #  output
		self.threads = threads  # number of threads
		self.UA = ""  # here will be UA loadaded from config
		self.countries = {}  # proxy list {"country":["proxy1"...]}
		self.hidecode = hidecode  # do not show response w/ this http codes
		self.showonly = showonly  # show response w/ this http codes
		self.version = version
		if File:
			self.url_dict = {}  # loaded from file

	def banner(self):
		print(f"{Fore.GREEN}Running AFTeam ShellHunt {self.version}{Style.RESET_ALL}")
		if self.phishings_file:
			print(f"\tLoaded {Fore.GREEN}{self.phishings_file}{Style.RESET_ALL}")
		else:
			print(f"\tLoaded {Fore.GREEN}{self.URL}{Style.RESET_ALL}")

		if self.save:
			print(f"\tSaving to {Fore.GREEN}{self.save}{Style.RESET_ALL}")

		if self.hidecode:
			print(f"\tNot showing responses with HTTP status {Fore.RED}{self.hidecode}{Style.RESET_ALL}")
		if self.showonly:
			print(f"\tShowing only responses with HTTP status {Fore.GREEN}{self.showonly}{Style.RESET_ALL}")
		print(f"\tRunning {Fore.RED}{self.threads}{Style.RESET_ALL} threads")

	def parse_config(self):
		config = configparser.RawConfigParser()
		try:
			config.read("deps/config.txt")
		except Exception as e:
			print(f"{Fore.RED}Corrupted config file!{Style.RESET_ALL}")
			print(e)
			exit(1)

		self.countries = dict(config.items('PROXIES'))  # read proxys from config

		if len(self.countries):
			for key in self.countries:
				self.countries[key] = self.countries[key].split(',')  # return {"country": ["proxies"]}
				# random.choice(self.countries[country])

	def start(self):
		self.banner()
		self.parse_config()