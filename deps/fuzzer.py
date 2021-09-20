
import configparser
from colorama import Fore, Style
from random import choice
import threading
import re
from deps.requester import request_bf
from requests import get as make_request

class Fuzzing:

	def __init__(self, target):
		self.target = target 
		self.memory_loaded_shells = []
		try:
			with open(target.shellfile) as f:
				self.memory_loaded_shells = f.readlines()
		except FileNotFoundError:
			print(f"File {target.shellfile} not found, did you create a shell list?")
			exit()
	def start_fuzz(self):
		if not self.target.phishings_file:
			self.banner()
			lines = sum(1 for line in open(self.target.shellfile, encoding = "ISO-8859-1"))
			chunks = int(lines / self.target.threads)
			add_odd = lines % self.target.threads
			if self.create_threads(lines, chunks, add_odd)==2:
				print(f"\n{Fore.RED}{self.target.URL} is not responding!{Style.RESET_ALL}")

		else:
			self.parse_config() # loads URL file
			self.banner()  # prints banner w/ info
			self.parseEachURL()  # foreach URL in File asign to target class then find_shell foreach URL

	def banner(self):

		print(f"{Fore.GREEN}Running AF-Team ShellHunt {self.target.version}{Style.RESET_ALL}\n")

		if not self.target.URL:
			print(f"\tURLs File:\t{Fore.GREEN}{self.target.phishings_file}{Style.RESET_ALL}")
		else:
			print(f"\tURL:\t{Fore.GREEN}{self.target.URL}{Style.RESET_ALL}")

		if self.target.save:
			print(f"\tSaving to:\t{Fore.GREEN}{self.target.save}{Style.RESET_ALL}")

		if not self.target.phishings_file:
			if self.target.hidecode:
				print(f"\tNot showing:\t{Fore.RED}{str(self.target.hidecode)[1:-1]}{Style.RESET_ALL}")
			if self.target.showonly:
				print(f"\tShowing only:\t{Fore.GREEN}{str(self.target.showonly)[1:-1] }{Style.RESET_ALL}")
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
		try:
			config = configparser.RawConfigParser(delimiters=('->'))
			config.read(self.target.phishings_file)
			self.target.phishing_list = config # load sites from user file, separated by countries ( to use proxy )
		except Exception as e:
			print(f"{Fore.RED}Corrupted config file!{Style.RESET_ALL}")
			print(f"{Fore.RED}Did you wrote '->' in all URLs?{Style.RESET_ALL}")
			print(e)
			exit(1)

	def parser_options_config_file(self, string):  
		values = string.split(",")
		self.target.hidecode, self.target.showonly, self.target.search_string, self.target.donotsearch_string, self.target.regex, self.target.dont_regex = [[],[200,302],False,False,False,False]
		print(f"\n\n\tAttacking:\t{Fore.RED}{self.target.URL}{Style.RESET_ALL}")

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
					print(f"\tShowing only coincidences with:\t{Fore.RED}{self.target.search_string}{Style.RESET_ALL}")

			if "show-regex" in i:

				regex = ''.join(re.findall('"([^"]*)"', i))

				if "not" in i:
					self.target.dont_regex = regex
					print(f"\tNot showing coincidence with:\t{Fore.RED}{self.target.dont_regex}{Style.RESET_ALL}")
				else:
					self.target.regex = regex
					print(f"\tShowing only coincidence with:\t{Fore.GREEN}{self.target.regex}{Style.RESET_ALL}")

	def create_threads(self, lines, chunks, add_odd):
		threads = []
		seek = 0
		try:

			make_request(self.target.URL if self.target.URL.startswith("http") else "http://" + self.target.URL)  # check if up
		except:
			return 2

		for worker in range(0, self.target.threads):

			if worker==self.target.threads-1 and add_odd:
				t = threading.Thread(target=request_bf, args=(self.target,self.memory_loaded_shells[seek:seek+chunks+add_odd],))
				threads.append(t)
				t.start()
				t.join()
			else:
				t = threading.Thread(target=request_bf, args=(self.target,self.memory_loaded_shells[seek:seek+chunks],))
				threads.append(t)
				t.start()

			seek+=chunks  # for each worker just read part of file

	def parseEachURL(self): # foreach URL in file parse country and parameters to target class, then find shell
		# for url in list do
		lines = sum(1 for line in open(self.target.shellfile, encoding = "ISO-8859-1"))

		chunks = int(lines / self.target.threads)
		add_odd = lines % self.target.threads

		for country in self.target.phishing_list:

			if country in self.target.countries or country == "noproxy":
				if country == "noproxy":
					self.target.usingProxy = False
				else:
					self.target.usingProxy = country

				for url in self.target.phishing_list[country]:
					self.target.URL = url
					self.parser_options_config_file(self.target.phishing_list[country][url])

					# threading start 

					if self.create_threads(lines, chunks, add_odd)==2:
						print(f"\n{Fore.RED}{self.target.URL} is not responding!{Style.RESET_ALL}")


			elif country != "DEFAULT":
				print(f"\n{Fore.RED}the country {country} is not in the conf file!{Style.RESET_ALL}")
				exit()