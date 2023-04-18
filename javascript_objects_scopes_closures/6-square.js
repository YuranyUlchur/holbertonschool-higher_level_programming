#!/usr/bin/node
// import file
const inhe = require('./5-square.js');
module.exports = class Square extends inhe {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    // Imprimimos el cuadrado con el carácter especificado
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
