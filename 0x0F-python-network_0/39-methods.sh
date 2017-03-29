#!/bin/bash
# display all methods server will accept
curl -sI "$1" | grep 'Allow' | cut -d ' ' -f2,3,4
