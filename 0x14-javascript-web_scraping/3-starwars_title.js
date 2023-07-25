#!/usr/bin/node

const request = require('request');

function getStarWarsEpisode () {
  const argsLen = 3;
  const ep = 2;
  const url = 'https://swapi-api.alx-tools.com/api/films/';

  if (process.argv.length !== argsLen) {
    console.log('Expected to receive one argument');
    return;
  }

  const endPoint = url + process.argv[ep];

  request(endPoint, (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }

    if (res && res.statusCode) {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
}

getStarWarsEpisode();
