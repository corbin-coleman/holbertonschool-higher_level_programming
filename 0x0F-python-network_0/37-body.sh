#!/bin/bash
# Display body of a response to GET request, only if it's a redirect
curl -L -s -X GET "$1"
