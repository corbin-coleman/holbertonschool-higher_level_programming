#!/usr/bin/node

let firstArg = process.argv[2];
let is = ' is ';
let secondArg = process.argv[3];

if (firstArg === undefined) {
  firstArg = 'undefined';
}
if (secondArg === undefined) {
  secondArg = 'undefined';
}

let printString = firstArg.concat(is).concat(secondArg);
console.log(printString);
