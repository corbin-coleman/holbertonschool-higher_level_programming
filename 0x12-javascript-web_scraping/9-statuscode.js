#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log('code:', response.statusCode);
});
