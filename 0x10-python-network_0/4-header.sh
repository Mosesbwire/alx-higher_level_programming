#!/bin/bash
# Sends a GET request with a custom header
curl -s -H X-School-User-Id:98 -X GET "$1"
