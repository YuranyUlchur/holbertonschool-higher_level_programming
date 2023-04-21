#!/usr/bin/node
// script that adds a li element to a list
$('#add_item').click(function () {
  $('.my_list').append('<li>Item</li>');
});
