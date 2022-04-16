#!/usr/bin/node

// The parseInt function checks the first argument,
// of a string, and attempts to return an integer of the specified base

const args = process.argv;
if (parseInt(args[2])) {
  console.log('My number: ' + args[2]);
} else {
  console.log('Not a number');
}
