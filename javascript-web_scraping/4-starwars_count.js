#!/usr/bin/node
// script that prints the number of movies
const request = require('request'); // Requerir el módulo 'request'

// Get the API URL or use the default URL
const apiUrl = process.argv[2] || 'https://swapi-api.hbtn.io/api/films/';

// Make the API request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Ocurrió un error al hacer la solicitud:');
    console.log(error);
  } else {
    // objets of the body
    const filmsData = JSON.parse(body).results;
    const wedgeAntillesFilms = filmsData.filter(film => {
      // Filter the movies
      return film.characters.includes('https://swapi-api.hbtn.io/api/people/18/');
    });
    // Print the number of films
    console.log(`${wedgeAntillesFilms.length}`);
  }
});
