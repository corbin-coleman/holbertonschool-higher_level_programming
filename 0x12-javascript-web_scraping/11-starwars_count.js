#!/usr/bin/node

const request = require('request');
const baseURL = process.argv[2];

request(baseURL, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  let films = JSON.parse(body)['results'];
  let count = 0;
  for (let i = 0; i < films.length; i++) {
    let filmDict = films[i];
    let filmCharacters = filmDict['characters'];
    for (let j = 0; j < filmCharacters.length; j++) {
      if (filmCharacters[j].match(/18/)) {
        count++;
      }
    }
  }
  console.log(count);
});
