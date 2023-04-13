#!/usr/bin/node
// Value of my argument
const numArgs = process.argv[2];

if (numArgs) {
  console.log(numArgs);
} else {
  console.log('No argument');
}
