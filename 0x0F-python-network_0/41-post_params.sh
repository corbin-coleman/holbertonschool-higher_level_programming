#!/bin/bash
# Send POST request, set body variables
curl -LsX POST -d email=hr@holbertonschool.com -d 'subject=I will always be here for PLD' "$1"
