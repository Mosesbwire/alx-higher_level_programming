#!/usr/bin/node

const fs = require('fs');

function writeToFile () {
  const argsLen = 4;
  const file = 2;
  const text = 3;

  if (process.argv.length !== argsLen) {
    console.log('Expected to receive two arguments.');
    return;
  }
  const filePath = process.argv[file];
  const content = process.argv[text];

  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) console.log(err);
  });
}

writeToFile();
