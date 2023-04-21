#!/usr/bin/node
// script that toggles the class of the header element
$('#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
