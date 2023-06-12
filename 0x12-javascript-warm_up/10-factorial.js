#!/usr/bin/node

function factorial(n) {
    if (n === 1) return 1

    return n * factorial(n - 1)
}

const factor = parseInt(process.argv[2])

if (!Number.isInteger(factor)) {
    console.log('1')
    return
}

let results = factorial(factor)
console.log(results)
