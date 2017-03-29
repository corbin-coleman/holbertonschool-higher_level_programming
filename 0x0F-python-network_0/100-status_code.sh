#!/bin/bash
# Display status code
curl -si "$1" | head -1 | cut -d ' ' -f2
