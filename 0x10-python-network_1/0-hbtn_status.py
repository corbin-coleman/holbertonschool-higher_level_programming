#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    print("Body response:")
    print("\t- type:", response.read())
    print("\t- content:", response.read())
    print("\t- utf8 content:", response.read().decode('utf-8'))
