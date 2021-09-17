from colorama import Fore, Style

class scanner:
	def __init__(self, URL, File, Save, threads):
		self.URL = URL
		self.phishings_file = File
		self.save = Save
		self.threads = threads

		if File:
			self.url_dict = {}  # loaded from file

	def banner(self):
		print(f"{Fore.GREEN}Running AFTeam ShellHunt{Style.RESET_ALL}")
		if self.phishings_file:
			print(f"\tLoaded {Fore.GREEN}{self.phishings_file}{Style.RESET_ALL}")
		else:
			print(f"\tLoaded {Fore.GREEN}{self.URL}{Style.RESET_ALL}")

		if self.save:
			print(f"\tSaving to {Fore.GREEN}{self.save}{Style.RESET_ALL}")

		print(f"\tRunning {Fore.RED}{self.threads}{Style.RESET_ALL} threads")


	def start(self):
		self.banner()