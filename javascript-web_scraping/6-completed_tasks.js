#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  // converts a string to an object
  const json = JSON.parse(body);
  // a dictionary is created to store the tasks completed by the user
  const dict = {};
  // to iterate over each user object in the JSON object.
  for (const userd of json) {
    const saveId = userd.userId;
    if (userd.completed) {
      if (dict[saveId]) {
        dict[saveId]++;
      } else {
        dict[saveId] = 1;
      }
    }
  }
  // print the dictionary
  console.log(dict);
});
