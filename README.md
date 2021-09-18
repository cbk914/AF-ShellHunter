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
# use not for not showing X ( as --hide )

# show-response-code -> show response with those status codes -sc
# show-string -> show match w/ that string -ss
# show-regex -> show math w/ regex -sr

#example


[peru]
phishingmalicioso.es: show-response-code "302" "200",not show-string "not found"

```

# Other features

1. Filter by [regex](https://regex101.com/)
2. Filter by string
3. Filter by HTTP Status code
4. Custom UA
5. Custom proxy or proxy block for URL file
6. Multithreading ( custom workers number )
