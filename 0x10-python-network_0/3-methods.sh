#!/bin/bash
# Diplays the http methods a server will accept
curl -sI "$1" | grep -i Allow | awk '{gsub("Allow: ", ""); print}
