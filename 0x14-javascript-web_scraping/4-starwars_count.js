#!/usr/bin/node
// Script to print the number of movies where "Wedge Antilles" is present

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';

if (!apiUrl) {
  console.error('Error: No API URL provided');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.endsWith(`/${wedgeAntillesId}/`)) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
