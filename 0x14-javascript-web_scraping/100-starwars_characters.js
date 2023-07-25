#!/usr/bin/node

const request = require('request');

function fetchMovie (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      }

      resolve(JSON.parse(body));
    });
  });
}

function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      }

      resolve(JSON.parse(body));
    });
  });
}

async function run () {
  const args = 3;
  const id = 2;
  if (process.argv.length === args) {
    const movieId = process.argv[id];
    const movieData = await fetchMovie(movieId);
    const characterUrls = movieData.characters;

    const characterPromises = [];

    characterUrls.forEach(url => {
      characterPromises.push(fetchCharacter(url));
    });

    const characterData = await Promise.all(characterPromises);

    characterData.forEach(character => {
      const data = character;
      console.log(data.name);
    });
  } else {
    console.log('Error: Expected to receive one argument');
  }
}

run();
