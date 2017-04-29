#!/usr/bin/node

const request = require('request');
const episodeId = process.argv[2];

request('http://swapi.co/api/films/'.concat(episodeId), function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log(JSON.parse(body)['title']);
});
