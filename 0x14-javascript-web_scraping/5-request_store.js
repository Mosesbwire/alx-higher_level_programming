#!/usr/bin/node

const fs = require('fs');
const request = require('request');

function fetchPage (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      }
      resolve(body);
    });
  });
}

function writeToFile (file, data) {
  fs.writeFile(file, data, 'utf-8', (err) => {
    if (err) {
      return err;
    }
  });
}

async function run () {
  const args = 4;
  const urlArg = 2;
  const fileArg = 3;

  if (process.argv.length === args) {
    const url = process.argv[urlArg];
    const data = await fetchPage(url);

    const file = process.argv[fileArg];
    writeToFile(file, data);
  } else {
    console.log(`Expected two arguments, received: ${process.argv.length - 2}`);
  }
}

run();
