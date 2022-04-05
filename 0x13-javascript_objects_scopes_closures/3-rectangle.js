#!/usr/bin/node
// The constructor must takes 2 arguments w and h
// If w or h is equal to 0 or not a positive integer, create an empty object
// same as task3 adding an instance method
// called print() that prints the rectangle using the character X
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height - 1) + 'X'.repeat(this.width));
  }
}
module.exports = Rectangle;
