#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
let data;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    data = JSON.parse(body);
    data.results.forEach(function (result) {
      result.characters.forEach(function (character) {
        const split = character.split('/');
        if (split[split.length - 2] === '18') {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
