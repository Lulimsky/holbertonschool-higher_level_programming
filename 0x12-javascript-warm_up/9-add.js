#!/usr/bin/node
function add (a, b) {
  const addition = a + b;
  console.log(addition);
}

add(Number(process.argv[2]), Number(process.argv[3]));
