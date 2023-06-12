#!/usr/bin/node

let content;

if (process.argv.length > 3) {
    content = 'Arguments found'
} else if (process.argv.length === 3) {
    content = 'Argument found'
} else {
    content = 'No argument'
}

console.log(content)

