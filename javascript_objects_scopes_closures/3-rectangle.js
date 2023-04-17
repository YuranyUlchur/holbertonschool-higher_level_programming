#!/usr/bin/node
// defines a rectangle:
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // creation of method
  print () {
    /*
    repeat() print the amount width in characters
    "X" on each line, and repeat this line height
    */
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
