#!/bin/bash
# display all methods server will accept
curl -si "$1" | grep 'Allow:' | cut -d ':' -f2 | cut -b2-
