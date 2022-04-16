#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  charPrint (character) {
    if (!character) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(character.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
