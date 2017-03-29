#!/usr/bin/python3
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isalpha():
        print('No result')
    else:
        q = {'q': sys.argv[1]}
        req = requests.post('http://0.0.0.0:5000/search_user', data=q)
        try:
            print('[{}] {}'.format(req.json()['id'], req.json()['name']))
        except Exception:
            print('Not a valid JSON')
