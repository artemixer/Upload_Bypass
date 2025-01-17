#!/usr/bin/env python3

from lib.update import get_current_version

# \033[1m is for a bold text
# \033[0m for a reset
# \033[1m\033[4m is for a bold and underline text

current_version = get_current_version()


def banner():
    tool_banner = f"""\033[1m  
_ _       _              _   ___                        
| | | ___ | | ___  ___  _| | | . > _ _  ___  ___  ___ ___
| ' || . \| |/ . \<_> |/ . | | . \| | || . \<_> |<_-<<_-<
`___'|  _/|_|\___/<___|\___| |___/`_. ||  _/<___|/__//__/
     |_|                          <___'|_|  {current_version}             
\033[0m

A Simple Tool for bypassing upload restriction in web applications by Sagiv Michael.

Usage: Upload Bypass [OPTIONS]

\033[1m\033[4mOptions:\033[0m
  \033[1m-h, --help\033[0m     Print help (see more with '--help')
  \033[1m-v, --version\033[0m  Print version

\033[1m\033[4mRequired Arguments:\033[0m 
  \033[1m-r, --request_file\033[0m <REQUEST_FILE>    Provide a request file to be proccessed
  \033[1m-E, --extension\033[0m    <EXTENSION>       Forbidden extension to check (ex: php)

  \033[1mChoose only one from the options below\033[0m:
  \033[1m-s, --success\033[0m      <MESSAGE>         Provide a failure message when a file is uploaded (ex: File was uploaded successfully)
  \033[1m-f, --failure\033[0m      <MESSAGE>         Provide a failure message when a file is uploaded (ex: File is not allowed!)
  \033[1m-S, --status_code\033[0m  <STATUS_CODE>     Provide a status code for a success upload (ex: 200)

\033[1m\033[4mMode Settings:\033[0m 
  \033[1m-d, --detect\033[0m          Upload harmless sample files (Suitable for a real penetration test)
  \033[1m-e, --exploit\033[0m         Upload Web-Shells files when testing
  \033[1m-a, --anti_malware\033[0m    Upload Anti-Malware Test file (Eicar) when testing
      \033[1mI.\033[0m  If set with -E flag the program will test with the Eicar string along with the \033[1mchoosen\033[0m extension
      \033[1mII.\033[0m If set without the -E flag the program will test with Eicar string and a \033[1mcom\033[0m extension

\033[1m\033[4mModules Settings:\033[0m     
  \033[1m-l, --list\033[0m            List all modules  
  \033[1m-i, --include_only\033[0m <MODULES>   Include only modules to test from (ex: extension_shuffle, double_extension)
  \033[1m-x, --exclude\033[0m      <MODULES>   Exclude modules (ex: svg_xxe, svg_xss)

\033[1m\033[4mRequest Settings:\033[0m 
  \033[1m--base64\033[0m              Encode the file data with Base64 algorithm
  \033[1m--allow_redirects\033[0m     Follow redirects
  \033[1m-P, --put\033[0m             Use the HTTP PUT method for the requests (Default is POST)
  \033[1m-R, --response\033[0m        Print the response to the screen
  \033[1m-c, --continue\033[0m        Continue testing all files, even if a few uploads encountered success
  \033[1m-rl, --rate_limit\033[0m <NUMBER>  Set a rate-limit with a delay in milliseconds between each request

\033[1m\033[4mProxy Settings:\033[0m 
  \033[1m-p, --proxy\033[0m <PROXY>   Proxy to use for requests (ex: http(s)://host:port, socks5(h)://host:port)
  \033[1m-k, --insecure\033[0m        Do not verify SSL certificates
  \033[1m--burp\033[0m                Set --proxy to 127.0.0.1:8080 and set --insecure to false

\033[1m\033[4mOptional Settings:\033[0m 
  \033[1m-D, --upload_dir\033[0m <UPLOAD_DIR>  Provide a remote path where the Web-Shell should be uploaded (ex: /uploads)
  \033[1m-o, --output\033[0m  <OUTPUT_PATH>    Output file to write the results into - Default current directory (ex: ~/Desktop/results.txt)
  \033[1m--debug\033[0m  <NUM>               Debug mode - Print the stack trace error to the screen and save it to a file (ex: --debug 1)
      \033[1mI.\033[0m  Level 1 - Saves only the stack trace error (default).
      \033[1mII.\033[0m Level 2 - Saves the stack trace error and user's arguments along with the request file.
  
\033[1m\033[4mResume settings:\033[0m
  \033[1m--resume\033[0m  <STATE_FILE>  State file from which to resume a partially complete scan

\033[1m\033[4mUpdate settings:\033[0m
  \033[1m-u, --update\033[0m  Update the program to the latest version"""
    print(f"{tool_banner}")