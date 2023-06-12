#!/usr/bin/node

if (process.argv.length <= 3) {
    console.log(0)
    return
}

const array = process.argv.splice(2)

array.sort((a, b) => {
    return b - a
})

console.log(array[1])
