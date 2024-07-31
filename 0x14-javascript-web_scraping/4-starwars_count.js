#!/usr/bin/node
// Script to print the number of movies where "Wedge Antilles" is present

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: No API URL provided');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeId = '18';
  let count = 0;

  films.forEach((film) => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
      count++;
    }
  });

  console.log(count);
});
