#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(file, body, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
