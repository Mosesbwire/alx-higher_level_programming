#!/usr/bin/node

str = 'C is fun'
const x = parseInt(process.argv[2])

if (!Number.isInteger(x)) {
    console.log('Missing number of occurrences')
    return
}

for (let y = 0; y < x; y++) {
    console.log(str)
}
