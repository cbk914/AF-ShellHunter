import configparser
from colorama import Fore, Style

class Fuzzing:

	def __init__(self, target):

		if len(dir(target)) == 41:
			self.target = target 
			self.banner()

		else:
			self.target = target	
			self.parse_config(target)
			self.banner()

	def banner(self):
		print(f"{Fore.GREEN}Running AF-Team ShellHunt {self.target.version}{Style.RESET_ALL}")
		if not self.target.URL:
			print(f"\tURLs File:\t{Fore.GREEN}{self.target.phishings_file}{Style.RESET_ALL}")
		else:
			print(f"\tURL:\t{Fore.GREEN}{self.target.URL}{Style.RESET_ALL}")

		if self.target.save:
			print(f"\tSaving to:\t{Fore.GREEN}{self.target.save}{Style.RESET_ALL}")

		if self.target.hidecode:
			print(f"\tNot showing\t{Fore.RED}{str(self.target.hidecode)[1:-1]}{Style.RESET_ALL}")
		if self.target.showonly:
			print(f"\tShowing only\t{Fore.GREEN}{str(self.target.showonly)[1:-1] }{Style.RESET_ALL}")
		print(f"\tThreads:\t{Fore.GREEN}{self.target.threads}{Style.RESET_ALL}")

		if self.target.search_string:
			print(f"\tShowing only coincidence with:\t{Fore.GREEN}{self.target.search_string}{Style.RESET_ALL}")
		if self.target.donotsearch_string:
			print(f"\tNot showing coincidence with:\t{Fore.RED}{self.target.donotsearch_string}{Style.RESET_ALL}")
		if self.target.regex:
			print(f"\tShowing only coincidence with:\t{Fore.GREEN}{self.target.regex}{Style.RESET_ALL}")
		if self.target.dont_regex:
			print(f"\tNot showing coincidence with:\t{Fore.RED}{self.target.dont_regex}{Style.RESET_ALL}")


	def parse_config(self, object):
		pass

	def find_shell(self): # Fuzz URL and Filter w/ passed arguments hc,hs, threads...
		pass