#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else if (num) {
    return factorial(num - 1) * num;
  }
  return 1;
}

let num = parseInt(process.argv[2]);

console.log(factorial(num));
