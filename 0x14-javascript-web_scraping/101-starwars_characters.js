#!/usr/bin/node
// Script to print all characters of a Star Wars movie in order

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Error: No Movie ID provided');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const getCharacterNames = async (urls) => {
    for (const url of urls) {
      await new Promise((resolve, reject) => {
        request(url, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error:', charError);
            reject(charError);
          } else if (charResponse.statusCode !== 200) {
            console.error(`Error: ${charResponse.statusCode}`);
            reject(new Error(`HTTP status ${charResponse.statusCode}`));
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
            resolve();
          }
        });
      });
    }
  };

  getCharacterNames(characters);
});
