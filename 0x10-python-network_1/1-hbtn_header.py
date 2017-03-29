#!/usr/bin/python3
import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        info = response.info()
        print(info.get('X-Request-Id'))
