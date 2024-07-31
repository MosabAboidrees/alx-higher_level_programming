#!/usr/bin/node
// Script to print the title of a Star Wars movie by episode number

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Error: No movie ID provided');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
