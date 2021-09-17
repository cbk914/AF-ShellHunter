import configparser
from colorama import Fore, Style
from random import choice
import re

class Fuzzing:

	def __init__(self, target):
		self.target = target 

		if not self.target.phishings_file:
			self.banner()

		else:
			self.parse_config() # loads URL file
			self.banner()
			
			self.parseEachURL()  # foreach URL in File asign to target class then attack


	def banner(self):

		print(f"{Fore.GREEN}Running AF-Team ShellHunt {self.target.version}{Style.RESET_ALL}")

		if not self.target.URL:
			print(f"\tURLs File:\t{Fore.GREEN}{self.target.phishings_file}{Style.RESET_ALL}")
		else:
			print(f"\tURL:\t{Fore.GREEN}{self.target.URL}{Style.RESET_ALL}")

		if self.target.save:
			print(f"\tSaving to:\t{Fore.GREEN}{self.target.save}{Style.RESET_ALL}")

		if not self.target.phishings_file:
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
			if self.target.usingProxy:
				print(f"\tProxy:\t{Fore.GREEN}{str(self.target.usingProxy)}{Style.RESET_ALL}")

		if self.target.phishing_list:  # prints used proxies when ph file loaded
			print_countries = []
			for i in self.target.phishing_list:
				if i != "DEFAULT":
					print_countries.append(i)
			print(f"\tProxy:\t{Fore.GREEN}{str(print_countries)[1:-1]}{Style.RESET_ALL}")	


	def parse_config(self):
		config = configparser.RawConfigParser()
		config.read(self.target.phishings_file)
		self.target.phishing_list = config # load sites from user file, separated by countries ( to use proxy )


	def check_string(self, html, donot=True):
		pass  # if ddnot is False Just do inverse

	def check_regex(self,html, donot=True):
		pass
	def check_status(self,status_code, donot=True):
		pass

	def verification(self, request):

		if self.target.search_string:
			if not self.check_string(request.text):
				return 0

		if self.target.donotsearch_string:
			if not self.check_string(False, request.text):
				return 0

		if self.target.self.target.regex:
			if not self.check_regex(request.text):
				return 0


		if self.target.dont_regex:
			if not self.check_string(request.text, False):
				return 0

		if self.target.hidecode:
			if not self.check_status():
				return 0

		if self.target.showonly:
			if not self.check_status(False):
				return 0

		return 1

	def find_shell(self):
		chunks = 1


	def parser_options_config_file(self, string):  
		values = string.split(",")
		self.target.hidecode, self.target.showonly, self.target.search_string, self.target.donotsearch_string, self.target.regex, self.target.dont_regex = [[],[200,302],False,False,False,False]
		print(f"\n\tAttacking:\t{Fore.RED}{self.target.URL}{Style.RESET_ALL}")
		for i in values:
			i = str(i.strip())

			if "show-response-code" in i:
				codes = re.findall('"([^"]*)"', i)
				if "not" in i:
					self.target.hidecode = [ int(x) for x in codes ]
					print(f"\tNot showing\t{Fore.RED}{str(self.target.hidecode)[1:-1]}{Style.RESET_ALL}")
				else:
					self.target.showonly = [ int(x) for x in codes ]
					print(f"\tShowing only\t{Fore.RED}{str(self.target.showonly)[1:-1]}{Style.RESET_ALL}")

			if "show-string" in i:
				string = ''.join(re.findall('"([^"]*)"', i))

				if "not" in i:
					self.target.donotsearch_string = string
					print(f"\tNot showing coincidence with:\t{Fore.RED}{self.target.donotsearch_string}{Style.RESET_ALL}")

				else:
					self.target.search_string = string
					print(f"\tShowing only coincidences with:\t{Fore.RED}{self.target.donotsearch_string}{Style.RESET_ALL}")

			if "show-regex" in i:

				regex = ''.join(re.findall('"([^"]*)"', i))

				if "not" in i:
					self.target.dont_regex = regex
					print(f"\tNot showing coincidence with:\t{Fore.RED}{self.target.dont_regex}{Style.RESET_ALL}")
				else:
					self.target.regex = regex
					print(f"\tShowing only coincidence with:\t{Fore.GREEN}{self.target.regex}{Style.RESET_ALL}")
	def parseEachURL(self): # Fuzz URL and Filter w/ passed arguments hc,hs, threads...
		# for url in list do

		if self.target.phishing_list:

			for i in self.target.phishing_list:
				if i in self.target.countries:
					for j in self.target.phishing_list[i]:
						self.target.URL = j
						self.parser_options_config_file(self.target.phishing_list[i][j])
						self.find_shell()