#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        Body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(Body)))
        print("\t- content: {}".format(Body))
        print("\t- utf8 content: {}".format(Body.decode("utf-8")))
