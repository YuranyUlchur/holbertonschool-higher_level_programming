#!/usr/bin/node
// script that fetches the character name from an URL
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});
