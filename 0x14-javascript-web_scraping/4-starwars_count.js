#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films', (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  let count = 0;
  data.results.forEach(movie => {
    const characters = movie.characters;
    characters.forEach(character => {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') count++;
    });
  });
  console.log(count);
});
