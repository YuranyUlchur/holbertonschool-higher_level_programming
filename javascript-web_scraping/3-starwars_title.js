#!/usr/bin/node
// script that prints the title of a Star Wars movie
const request = require('request'); // Requerir el módulo 'request'

// Verify if the movie ID argument was provided
if (process.argv.length < 3) {
  process.exit(1);
}

// Get the movie ID from the third argument
const movieId = process.argv[2];
// Build API URL
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`; //

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // objets of the body
    const movieData = JSON.parse(body);
    // print title
    console.log(`${movieData.title}`);
  }
});
