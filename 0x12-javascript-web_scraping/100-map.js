#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
const newArray = list.map(function (x, index) {
  return x * index;
});
console.log(newArray);
