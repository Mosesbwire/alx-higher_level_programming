#!/usr/bin/node

const fs = require('fs');

function readData () {
  const argsLen = 3;

  if (process.argv.length !== argsLen) {
    console.log('Expected to receive one argument');
    return;
  }

  const filePath = process.argv[2];

  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
}

readData();
