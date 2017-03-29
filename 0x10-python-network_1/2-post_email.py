#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    email = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
