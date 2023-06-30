#!/bin/bash
# Make a POST request and display the params sent
curl -s -d 'email: test@gmail.com' -d 'subject: I will always be here for PLD' -X POST "$1"
