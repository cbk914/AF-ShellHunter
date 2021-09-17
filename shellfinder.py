 #!/usr/bin/python3
import argparse
from deps.scanner import scanner

__version__ = "1.0.1b"


class ShellFinder():
	def __init__(self, version):
		self.parser = argparse.ArgumentParser()
		self.group = self.parser.add_mutually_exclusive_group(required=True)
		self.group.add_argument('--url', '-u', action='store', dest='URL', help='URL to scan', default=False)
		self.group.add_argument('--file', '-f', action='store', dest='File',help='Phishings URL file', default=False)
		self.parser.add_argument('--proxy', '-p', action='store', dest='proxy', help='proxy country to use ( look deps/config.txt)', default=False)
		self.parser.add_argument('--save', '-s', action='store', dest='Save', help='Save to...', default=False)
		self.parser.add_argument('--threads', '-t', action='store', dest='threads', help='Threads to run, default 20', default=20)
		self.parser.add_argument('--hide-code', '-hc', action='store', dest='hidecode', help='Do not show responses w/ this code',nargs="+", type=int, default=[])
		self.parser.add_argument('--show-code', '-sc', action='store', dest='showonly', help='Do not show responses w/o this code',nargs="+", type=int, default=[200,302])
		self.parser.add_argument('--show-string', '-ss', action='store', dest='string', help='Do not show responses w/ this string', default=False)
		self.parser.add_argument('--hide-string', '-hs', action='store', dest='notstring', help='Do not show responses w/o this string', default=False)
		self.parser.add_argument('--show-regex', '-sr', action='store', dest='regex', help='Do not show responses w this regex', default=False)
		self.parser.add_argument('--hide-regex', '-hr', action='store', dest='notregex', help='Do not show responses w/o this regex', default=False)
		self.results = self.parser.parse_args()

		if not self.results.URL and not self.results.File:
			print("You have to input some URL")
		self.scan = scanner(version, self.results.URL, self.results.File, self.results.Save, self.results.threads,
			self.results.hidecode, self.results.showonly, self.results.proxy, self.results.string, self.results.notstring, self.results.regex,
			self.results.notregex)

		self.scan.start()

if __name__=="__main__":
	main = ShellFinder(__version__)