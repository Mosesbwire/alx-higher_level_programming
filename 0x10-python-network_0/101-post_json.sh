#!/usr/bin/bash
# Post a json file
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
