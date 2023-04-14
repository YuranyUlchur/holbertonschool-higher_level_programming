#!/usr/bin/node
//  An Integer
const arg1 = process.argv[2];
const arg = parseInt(arg1, 10);

if (!isNaN(arg)) {
  console.log('My number: ' + arg);
} else {
  console.log('Not a number');
}
