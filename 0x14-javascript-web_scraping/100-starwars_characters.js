#!/usr/bin/node
const request = require('request');
const ID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + ID;

request({ url: url, json: true }, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  const characters = body.characters;
  for (const line of characters) {
    request(line, (err, response, body) => {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
