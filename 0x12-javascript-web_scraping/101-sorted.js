#!/usr/bin/node

const idsOccurred = require('./101-data').dict;

let occurredIds = {};
for (let key in idsOccurred) {
  if (occurredIds[idsOccurred[key]]) {
    occurredIds[idsOccurred[key]].push(key);
  } else {
    occurredIds[idsOccurred[key]] = [];
    occurredIds[idsOccurred[key]].push(key);
  }
}
console.log(occurredIds);
