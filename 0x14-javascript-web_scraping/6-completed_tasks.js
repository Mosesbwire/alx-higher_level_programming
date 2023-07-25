#!/usr/bin/node

const request = require('request');

function fetchTodos (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      }
      resolve(JSON.parse(body));
    });
  });
}

function prepareData (data) {
  const userIdSet = new Set();
  const transformedData = {};

  const getUserIds = () => {
    data.forEach(todo => userIdSet.add(todo.userId));
  };

  getUserIds();

  userIdSet.forEach(id => {
    let completed = 0;

    data.forEach(todo => {
      if (todo.userId === id && todo.completed) {
        completed++;
        transformedData[todo.userId] = completed;
      }
    });
  });

  console.log(transformedData);
}

async function run () {
  const args = 3;
  const urlArg = 2;

  if (process.argv.length === args) {
    const url = process.argv[urlArg];
    const data = await fetchTodos(url);
    prepareData(data);
  } else {
    console.log('Passed wrong number of arguments');
  }
}

run();
