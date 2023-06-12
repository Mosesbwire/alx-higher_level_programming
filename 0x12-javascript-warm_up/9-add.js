#!/usr/bin/node

function add(a, b) {
   let results = a + b
    console.log(results)
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]))
