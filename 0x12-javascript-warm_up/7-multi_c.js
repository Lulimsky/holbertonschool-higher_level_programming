#!/usr/bin/node

// In JavaScript 'NaN' is short for "Not-a-Number".
// in this case 'isNaN()' method converts
// the value to a number before testing it.

let loop = 0;

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (loop < process.argv[2]) {
    console.log('C is fun');
    loop++;
  }
}
