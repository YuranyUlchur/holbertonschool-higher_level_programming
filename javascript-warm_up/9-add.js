#!/usr/bin/node
// script that prints the addition of 2 integers

const add = (a, b) => {
  const result = a + b;
  console.log(result);
};

const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

add(firstInteger, secondInteger);
