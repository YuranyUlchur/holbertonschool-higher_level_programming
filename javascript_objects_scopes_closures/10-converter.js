#!/usr/bin/node
//  Number conversion
exports.converter = function (base) {
    return val => val.toString(base);
  };