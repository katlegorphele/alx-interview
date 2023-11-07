#!/usr/bin/node
/* Fetch Data from starwars API */

const req = require('request');
const args = process.argv.slice(2);

const fetchData = (url) => {
  const promise = new Promise((resolve, reject) => {
    // send get request
    req.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        // console.log(`${response.statusCode}`);
        reject(new Error('Something Went Wrong!, Try Again'));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
  return promise;
};

const fetchStarWarsMovies = async (movieID) => {
  try {
    const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}/`;
    const data = await fetchData(apiUrl);
    const characters = data.characters;
    // console.log(characters)
    // loop through the characters array to get their names
    const charactersName = await Promise.all(
      characters.map(async (url) => {
        const character = await fetchData(url);
        return character.name;
      })
    );

    // console.log(charactersName);
    charactersName.forEach((name) => console.log(`${name}`));
  } catch (error) {
    console.log(error);
  }
};

const movieID = args[0];
fetchStarWarsMovies(movieID);
