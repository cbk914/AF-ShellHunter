import requests
from functools import wraps
from re import match as regex_in_html
from random import choice
import sys
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def verify(target, web_object):
	if target.search_string:
		if not check_string(target, web_object.text):
			return 0

	if target.donotsearch_string:
		if not check_string(target, web_object.text, False):
			return 0

	if target.regex:
		if not check_regex(target, web_object.text):
			return 0


	if target.dont_regex:
		if not check_regex(target, web_object.text, False):
			return 0

	if target.hidecode:
		if not check_status(target, web_object.status_code):
			return 0

	if target.showonly:
		if not check_status(target, web_object.status_code, False):
			return 0
	return 1

def check_string(target, html, donot=True):
	if donot:  # if string in html return 1
		if target.search_string.lower() in html.lower():
			return 1
		else:
			return 0
	else:  # if string in html return 0
		if target.donotsearch_string.lower() in html.lower():
			return 0
		else:
			return 1

def check_regex(target,html, donot=True):
	if donot:  # if string in html return 1
		if regex_in_html(target.regex, html):  # if regex match
			return 1
		else:
			return 0
	else:  # if string in html return 0
		if regex_in_html(target.dont_regex, html):  # if regex match
			return 0
		else:
			return 1


def check_status(target,status_code, donot=True):
	if donot:
		if status_code not in target.hidecode:
			return 1
		else:
			return 0

	else:
		if status_code in target.showonly:
			return 1
		else:
			return 0


def beautifyURL(a_func):  # decorator add http at start and / to end.
	@wraps(a_func)
	def wrapTheFunction(target, data):
		if not target.URL.endswith('/'):
			target.URL+="/"
		if not target.URL.startswith("http"):
			target.URL="http://"+target.URL
		a_func(target, data)
	return wrapTheFunction

@beautifyURL
def request_bf(target, data):

	for webdir in data:

		try:
			if target.usingProxy:
				proxy = choice(target.countries[target.usingProxy])
				proxyDict = {
					'http': "http://" + proxy,
					'https':"https://" +  proxy
				}
				web_object = requests.get(target.URL + webdir.replace("\n",""), proxies=proxyDict, headers=target.headers, verify=False, timeout=5)
			else:
				web_object = requests.get(target.URL + webdir.replace("\n",""),  headers=target.headers, verify=False, timeout=5)

		except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as err:
			print()
			print('Server taking too long. Check proxy')
			print(err)
		except Exception as e:
			print()
			print("Uncaught Exception: " + str(e))
		else:
			if verify(target, web_object):
				sys.stdout.flush()
				print(f"Found {target.URL}" + webdir.replace("\n",""))
				requests.get(target.URL + webdir.replace("\n",""),  headers=target.headers, verify=False, timeout=5)

				if target.save:
					with open(target.save, "a+") as f:
						f.writelines(target.URL + webdir.replace("\n", ""))
			else:
				#print(target.URL + webdir.replace("\n",""), end="\r")
				pass
"""			else:
				if webdir != data[-1]:
					print(target.URL + webdir.replace("\n",""), end="\r")
				else:
					sys.stdout.flush()
	"""