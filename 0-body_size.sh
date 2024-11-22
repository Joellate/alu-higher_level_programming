#!/bin/bash
Check if a URL is passed as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request using curl and get the response body size
curl -s "$1" | wc -c
