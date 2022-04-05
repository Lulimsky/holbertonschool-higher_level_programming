#!/usr/bin/node

// The constructor must takes 2 arguments w and h
// If w or h is equal to 0 or not a positive integer, create an empty object
// same as task3 adding an instance method
// called print() that prints the rectangle using the character X
module.exports = class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print (character) {
    character = 'X';
    for (let rect = 0; rect < this.height; rect++) {
      console.log(character.repeat(this.width));
    }
  }
};
