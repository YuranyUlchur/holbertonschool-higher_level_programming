#!/usr/bin/node
// script that computes and prints a factorial

const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

const argument = parseInt(process.argv[2]);
const result = factorial(argument);

console.log(result);
