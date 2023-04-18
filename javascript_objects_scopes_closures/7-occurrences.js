#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  // reduces is the number of occurrences of the element
  return (list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0));
};
