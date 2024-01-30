#!/usr/bin/node

/* Fetch Data from starwars API 
Display one character name per line in the 
same order as the “characters” list in the /films/ endpoint*/

const req = require("request");
const args = process.argv.slice(2);
const url = "https://swapi-api.hbtn.io/api/films/" + args[0];

req(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      req(character, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
