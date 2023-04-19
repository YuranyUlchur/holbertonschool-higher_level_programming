#!/usr/bin/node
// script that write and prints the content of a file
const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
