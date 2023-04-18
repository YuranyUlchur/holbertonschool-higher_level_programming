#!/usr/bin/node
let nExec = 0;
/*
function that prints the number of arguments
already printed and the new argument value
*/
exports.logMe = function (item) {
  console.log('%d: %s', nExec++, item);
};