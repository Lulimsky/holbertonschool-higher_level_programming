#!/usr/bin/node
class Rectangle {
  // 'constructor' is a special function that
  // creates and initializes an object instance of a class
  // purpose is to create a new object and set values for any existing object properties.
  // 'this' keyword begins to refer to the new object and it becomes the current instance object
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
