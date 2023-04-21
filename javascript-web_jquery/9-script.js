#!/usr/bin/node
/*
retrieves information from the URL
and displays the value of hello obtained
in the HTML tag DIV#hello.
*/
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('#hello').text(data.hello);
});
