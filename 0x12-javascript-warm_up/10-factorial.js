#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const argv = process.argv;

if (!argv[2] || !parseInt(argv[2])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(argv[2])));
}
