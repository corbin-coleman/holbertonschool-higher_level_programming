#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  let tasks = JSON.parse(body);
  let finished = {};
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i]['completed'] === true) {
      if (finished[tasks[i]['userId']]) {
        finished[tasks[i]['userId']]++;
      } else {
        finished[tasks[i]['userId']] = 1;
      }
    }
  }
  console.log(finished);
});
