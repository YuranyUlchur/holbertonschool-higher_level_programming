#!/usr/bin/node
// script that computes and prints a factorial

function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n < 0) {
    return NaN;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}

const n = parseInt(process.argv[2]);

console.log(computeFactorial(n));
