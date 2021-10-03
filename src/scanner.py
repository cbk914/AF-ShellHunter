import configparser

from colorama import Fore, Style

from src.fuzzer import Fuzzing


class Target:
    def __init__(self, version: str, arg_object: object):
        """
        current URL and its options are stored ( if -u class do not change; else deps.fuzzer.parser_options_config_file
        will change 4 each URL in urls_file)

        :param version: str containing af-shellhunter version
        :param arg_object: argparse object, with all user options
        """
        #  URL, File, Save, threads, hidecode, showonly, proxy_country, filterbystring, notshowstring, filterbyregex, notshowregex

        self.version = version
        self.URL = arg_object.URL  # URL ( when using --url )
        self.phishings_file = arg_object.File  # phishing file (when using --file)
        self.save = arg_object.Save  # save output here
        self.threads = arg_object.threads  # number of threads to run, default is 20
        self.hidecode = arg_object.hidecode  # do not show response w/ this http codes
        self.showonly = arg_object.showonly  # show response w/ this http codes
        self.usingProxy = arg_object.proxy  # current proxy to use
        self.search_string = arg_object.string
        self.donotsearch_string = arg_object.notstring
        self.regex = arg_object.regex
        self.dont_regex = arg_object.notregex
        self.min_chars = arg_object.showChars  # min number of chars to show results ( default False)
        self.max_chars = arg_object.hideChars  # max number of chars
        self.headers = {}  # here will be UA loadaded from config
        self.countries = {}  # proxy list {"country":["proxy1"...]}
        self.phishing_list = []  # URL file loaded
        self.shellfile = arg_object.shellfile


class scanner:
    def __init__(self, version: str, arg_object: object) -> None:
        self.target = Target(version, arg_object)

    def parse_config(self):
        """
        Parse config file and save to target self object
        :return: None
        """
        config = configparser.RawConfigParser(delimiters="?")

        try:
            config.read("user_files/config.txt")
        except Exception as e:
            print(f"{Fore.RED}Corrupted config file!{Style.RESET_ALL}")
            print(e)
            exit(1)

        self.target.countries = dict(
            config.items('PROXIES'))  # read proxys from config and save to using proxy countries
        if self.target.usingProxy and self.target.usingProxy not in self.target.countries:  # exit if country not in config file
            print(f"\n{Fore.RED}the country is not in the conf file!{Style.RESET_ALL}")
            exit(1)

        if len(self.target.countries):
            for key in self.target.countries:
                self.target.countries[key] = self.target.countries[key].split(',')  # return {"country": ["proxies"]}
        self.target.headers = dict(config.items('HEADERS'))  # read HEADERS from config

    def start(self) -> None:
        """
        Start main program
        """
        self.parse_config()  # parse config file, save Proxies and Headers into Target

        fuzz = Fuzzing(self.target)  # Instance of main program
        fuzz.start_fuzz()  # start module w/ user info alredy validated
