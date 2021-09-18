import requests
from functools import wraps
from re import match

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
		if not check_string(target, web_object.text, False):
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
		if target.search_string in html:
			return 1
		else:
			return 0
	else:  # if string in html return 0
		if target.donotsearch_string in html:
			return 0
		else:
			return 1

def check_regex(target,html, donot=True):
	if donot:  # if string in html return 1
		if match(target.regex, html):  # if regex match
			return 1
		else:
			return 0
	else:  # if string in html return 0
		if match(target.dont_regex, html):  # if regex match
			return 0
		else:
			return 1


def check_status(target,status_code, donot=True):
	if donot and status_code not in target.showonly:
		return 0
	if not donot and status_code in target.hidecode:
		return 0
	return 1

def beautifyURL(a_func):
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
			web_object = requests.get(target.URL + webdir.replace("\n",""), timeout=5)

		except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as err:
			return 'Server taking too long. Try again later'
		else:
			print(web_object.status_code)
			if verify(target, web_object):
				print("Found " + target.URL + webdir.replace("\n", ""))
		

def find_shell(target, from_line, to_line):

	with open(target.shellfile, "r", encoding = "ISO-8859-1") as f:
	    f.seek(from_line)
	    data = f.readlines(to_line - from_line)

	request_bf(target, data)
	#print(data)
	# we will need target.URL, target.save, target.usingProxy, target.countries, target.headers
	#si hay coincodencoa self.verification(), if True:
	# print result and if save, save