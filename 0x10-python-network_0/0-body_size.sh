#!/usr/bin/bash
# Sends a request to a url and displays the size of the body response
curl -sI "$1" | grep -i content-length | awk '{gsub("Content-Length: ", ""); print}'
