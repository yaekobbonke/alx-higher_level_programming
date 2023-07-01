#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    a = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(a.text)))
    print("\t- content: {}".format(a.text))
