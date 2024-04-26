#!/bin/bash
# sends a req to a URL and displays size of response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

