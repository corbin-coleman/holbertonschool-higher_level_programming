#!/bin/bash
# Display body of GET request, send heder variable
curl -LsX GET -H 'X-HolbertonSchool-User-Id: 98' "$1"
