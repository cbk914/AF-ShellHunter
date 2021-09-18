# AF-ShellHunter

![adshellhunter](https://user-images.githubusercontent.com/41192980/133873080-1cf088a6-f401-4e01-8171-b28898206e1a.png)
## AF-ShellHunter: Auto shell lookup
 AF-ShellHunter its a script designed to automate the search of WebShell's in AF Team
 
 # How to
 
 ```
 
 pip3 install -r requirements.txt
 python3 shellhunter.py --help
 
 ```

# Basic Usage

You can run shellhunter in two modes
* **--url -u** When scanning a single url
* **--file -f** Scanning multiple URLs at once

# File configuration for multiple sites

[phishing_list](user_files/phishing_list.txt)

```
# How to?
# set country block with [country], please read user_files/config.txt

# 'show-response-code' -> show responses with those status codes, as -sc
# 'show-string' -> show match with that string, as -ss
# 'show-regex' -> show match with regex, as -sr

# use 'not' for not showing X, as -h[option]

# Example searching webshell with Peru proxy required, 302, 200 status code and not showing results w/ 'página en mantenimiento'

[peru]
https://banco.phishing: show-response-code '302' '200', not show-string 'página en mantenimiento'

[noproxy]
banco.es: # ShellHunt will add 'http://'
```

# Other features

1. Filter by [regex](https://regex101.com/)
2. Filter by string
3. Filter by [HTTP Status code](https://developer.mozilla.org/es/docs/Web/HTTP/Status)
4. Custom [User-Agent](https://deviceatlas.com/blog/list-of-user-agent-strings)
5. Custom proxy or proxy block for URL file
6. Multithreading ( custom workers number )
