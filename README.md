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

 Example searching webshell with burpsuite proxy, hiding string "404"
```
┌──(blueudp㉿xxxxxxxx)-[~/AF-ShellHunter]
└─$ python3 shellhunter.py -u https://xxxxxxxxxx -hs "404" -p burp                                                                                             
Running AF-Team ShellHunt 1.1.0

        URL:    https://xxxxxxxxxx
        Showing only:   200, 302
        Threads:        20
        Not showing coincidence with:   404
        Proxy:  burp
Found https://xxxxxxxxxx/system.php

```

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

[burp]
https://banco.phishing->show-response-code '302' '200', not show-string 'página en mantenimiento'

[noproxy]
banco.es-> # ShellHunt will add 'http://'
```
# Setting your proxies and custom headers

[config.txt](user_files/config.txt)
```
[HEADERS]  # REQUESTS CUSTOM HEADERS, ADD 'OPTION: VALUE'
User-Agent? Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36

[PROXIES]
burp? 127.0.0.1:8080,127.0.0.1:8080  # random choice between proxies
```

# Other features

1. Filter by [regex](https://regex101.com/)
2. Filter by string
3. Filter by [HTTP Status code](https://developer.mozilla.org/es/docs/Web/HTTP/Status)
4. Custom [Headers](https://developer.mozilla.org/es/docs/Web/HTTP/Headers)
5. Custom proxy or proxy block for URL file
6. Multithreading ( custom workers number )
```
                                                              .-"; ! ;"-.
        ----.                                               .'!  : | :  !`.
        "   _}                                             /\  ! : ! : !  /\
        "@   >                                            /\ |  ! :|: !  | /\
        |\   7                                           (  \ \ ; :!: ; / /  )
        / `--                                           ( `. \ | !:|:! | / .' )
            ,-------,****                               (`. \ \ \!:|:!/ / / .')
  ~        >o<  \---------o{___}-            =>          \ `.`.\ |!|! |/,'.' /
 /  |  \  /  ________/8'                                 `._`.\\\!!!// .'_.'
 |  |        /        "                                      `.`.\\|//.'.'
 |  /     |                                                   |`._`n'_.'|
                                                              "----^----"
```
