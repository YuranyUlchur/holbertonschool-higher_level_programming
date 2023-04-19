#!/usr/bin/node
// script that display the status code of a GET request.
const request = require('request');

// Check if the URL argument was provided
if (process.argv.length < 3) {
  process.exit(1);
}

// Get the URL from the third argument
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
