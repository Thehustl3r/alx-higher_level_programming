#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) { process.exit(1); } else if (response.statusCode !== 200) { process.exit(1); } else {
    try {
      const movieData = JSON.parse(body);
      const characterId = 18;
      const moviesWithWedge = movieData.results.filter((movie) =>
        movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );
      console.log(moviesWithWedge.length);
    } catch (e) {
      process.exit(1);
    }
  }
});
