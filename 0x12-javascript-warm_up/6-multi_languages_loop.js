#!/usr/bin/node

// "let" is used to declare the i variable in a loop
// if i variable will only be visible within the loop.
// "for" loop allow us to iterate
// through a block of code a number of times

const args = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (let i = 0; i < 3; i++) {
  console.log(args[i]);
}
