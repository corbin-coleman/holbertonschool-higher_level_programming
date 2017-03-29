#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    fetched = response.read()
    print("Body response:")
    print("\t- type:", type(fetched))
    print("\t- content:", fetched)
    print("\t- utf8 content:", fetched.decode('utf-8'))
