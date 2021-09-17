#!/usr/bin/python3
import argparse
from deps.scanner import scanner

__version__ = "1.0.1b"


def main(version):
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--url', '-u', action='store', dest='URL', help='URL to scan')
	group.add_argument('--file', '-f', action='store', dest='File',help='Phishings file', default=False)

	parser.add_argument('--save', '-s', action='store', dest='Save', help='Save to', default=False)
	parser.add_argument('--threads', '-t', action='store', dest='threads', help='Threads to run, default 20', default=20)
	parser.add_argument('--hide-code', '-hc', action='store', dest='hidecode', help='Do not show responses w/ this code',nargs="+", type=int, default=[])
	parser.add_argument('--show-code', '-sc', action='store', dest='showonly', help='Do not show responses w/o this code',nargs="+", type=int, default=[200,302])
	results = parser.parse_args()

	if not results.URL and not results.File:
		print("You have to input some URL")
	scan = scanner(version, results.URL, results.File, results.Save, results.threads,
		results.hidecode, results.showonly)

	scan.start()

if __name__=="__main__":
	main(__version__)