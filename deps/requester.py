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

def check_string(self, html, donot=True):
	pass  # if ddnot is False Just do inverse

def check_regex(self,html, donot=True):
	pass
def check_status(self,status_code, donot=True):
	pass

def find_shell(target, from_line, to_line):
	print("linea: " + str(from_line) + " hasta " + str(to_line))
			#si hay coincodencoa self.verification(), if True:
					# print result and if save, save