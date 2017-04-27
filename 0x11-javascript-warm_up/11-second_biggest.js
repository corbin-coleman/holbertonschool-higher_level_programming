#!/usr/bin/node

if (process.argv.length > 3) {
  let numArray = [];
  let j = 0;
  for (let i = 2; i < process.argv.length; i++) {
    numArray[j] = process.argv[i];
    j++;
  }
  let largest = numArray[0];
  let nextLargest = numArray[1];
  for (let i = 0; i < numArray.length; i++) {
    if (numArray[i] > largest) {
      nextLargest = largest;
      largest = numArray[i];
    } else if (numArray[i] > nextLargest && numArray[i] < largest) {
      nextLargest = numArray[i];
    }
  }
  console.log(nextLargest);
} else {
  console.log(0);
}
