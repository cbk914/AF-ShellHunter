import configparser
from colorama import Fore, Style

class Fuzzing:

	def __init__(self, *arg):
		if len(arg) == 11	:
			self.URL = arg[0]  # URL to scan
			self.search_string = arg[1]  # False or string to grep
			self.notsearch_string = arg[2]  # False or string to inverse grep
			self.regex = arg[3]  # False or regex to grep
			self.dont_regex = arg[4] # False or regex to inverse grep
			self.hidecode = arg[5] # do not show this codes
			self.showonly = arg[6]  # show only http status code
			self.usingProxy = arg[7]  # False or COUNTRY to use, NOT proxy
			self.save = arg[8]
			self.version = arg[9]
			self.threads = arg[10]
			self.banner()

		else:
			self.parse_config(*arg)

	def banner(self):
		print(f"{Fore.GREEN}Running AF-Team ShellHunt {self.version}{Style.RESET_ALL}")
		if not self.URL:
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
		if self.notsearch_string:
			print(f"\tNot showing coincidence with:\t{Fore.RED}{self.notsearch_string}{Style.RESET_ALL}")
		if self.regex:
			print(f"\tShowing only coincidence with:\t{Fore.GREEN}{self.regex}{Style.RESET_ALL}")
		if self.dont_regex:
			print(f"\tNot showing coincidence with:\t{Fore.RED}{self.dont_regex}{Style.RESET_ALL}")


	def parse_config(self, *args):
		self.version = args[-1]
		self.banner()

	def find_shell(self): # Fuzz URL and Filter w/ passed arguments hc,hs, threads...
		pass