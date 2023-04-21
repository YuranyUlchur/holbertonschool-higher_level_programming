#!/usr/bin/node
// script that fetches and lists the title for all movies by using this URL
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const dict of data.results) {
    const txt2 = window.$('<li></li>').text(dict.title);
    $('#list_movies').append(txt2);
  }
});
