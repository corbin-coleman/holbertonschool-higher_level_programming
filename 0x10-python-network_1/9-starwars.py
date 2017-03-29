#!/usr/bin/python3
import requests
import sys


if __name__ == '__main__':
    search = sys.argv[1]
    req = requests.get('http://swapi.co/api/people/?search={}'.format(search))
    results = req.json()['results']
    print("Number of result: {}".format(req.json()['count']))
    for dics in results:
        print(dics['name'])
