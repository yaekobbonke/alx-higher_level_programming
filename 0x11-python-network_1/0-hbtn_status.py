#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    result = response.read()
    print(result) 

   # if __name__ == "__main__":
