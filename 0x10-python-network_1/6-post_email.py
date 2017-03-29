#!/usr/bin/python3
import requests
import sys


if __name__ == '__main__':
    emails = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=emails)
    print(req.text)
