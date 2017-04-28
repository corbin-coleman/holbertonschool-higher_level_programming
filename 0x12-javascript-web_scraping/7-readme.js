#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    const print_data = data.split('\n')[0];
    console.log(print_data);
  }
});
