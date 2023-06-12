#!/usr/bin/node

let sq = 'X'
const x = parseInt(process.argv[2])

if (!Number.isInteger(x)) {
    console.log('Missing size')
    return
}

for (let y = 0; y < x; y++) {
    let str = '';

    for (let z = 0; z < x; z++) {
        str += sq
    }
    console.log(str)
}
