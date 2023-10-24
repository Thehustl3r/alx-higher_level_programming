#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) { process.exit(1); } else if (response.statusCode !== 200) { process.exit(1); } else {
    try {
      const movieData = JSON.parse(body);
      if (movieData.title) { console.log(movieData.title); } else { process.exit(1); }
    } catch (e) {
      console.error(e);
    }
  }
});
