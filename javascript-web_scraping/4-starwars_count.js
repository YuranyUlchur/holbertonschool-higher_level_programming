#!/usr/bin/node
// script that prints the number of movies
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  err = 0;
  response = '';
  let count = 0;
  const json = JSON.parse(body);
  for (const films of json.results) {
    for (const people of films.characters) {
      if (people.includes('18')) { count++; }
    }
  }
  console.log(count);
});
