#!/usr/bin/node
// Prototype
exports.esrever = function (item) {
  // create list
  const newList = [];
  // scroll down the list
  for (let i = item.length - 1; i >= 0; i--) {
    // add element
    newList.push(item[i]);
  }
  return newList;
};
