#!/usr/bin/node
// import file
const Rectangle = require('./4-rectangle.js');

//  class Square
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
