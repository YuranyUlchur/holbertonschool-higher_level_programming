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

  rotate () {
    // Swap width and height values
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Multiply the value of width and height by 2
    this.width *= 2;
    this.height *= 2;
  }
};
