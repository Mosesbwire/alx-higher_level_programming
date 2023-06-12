#!/usr/bin/node

const num = parseInt(process.argv[2])

Number.isInteger(num)
    ? console.log('My number: ' + num)
    : console.log('Not a number')
