#!/usr/bin/node

const x = parseInt(process.argv[2]);
let str = '';

if (x) {
  if (x > 0) {
    for (let i = 0; i < x; i++) {
      str = str.concat('X');
    }
    for (let i = 0; i < x; i++) {
      console.log(str);
    }
  }
} else {
  console.log('Missing number of occurences');
}
