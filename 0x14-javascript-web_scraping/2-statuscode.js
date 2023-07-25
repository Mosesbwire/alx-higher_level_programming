#!/usr/bin/node

const request = require('request');

function get () {
  const argsLen = 3;
  const urlArg = 2;

  if (process.argv.length !== argsLen) {
    console.log('Expected to receive one argument');
    return;
  }
  const url = process.argv[urlArg];

  request(url, (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log('code:', res && res.statusCode);
  });
}

get();
