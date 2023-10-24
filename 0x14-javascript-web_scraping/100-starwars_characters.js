#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(
  apiUrl,
  (error, response, body) => {
    if (error) { process.exit(1); } else if (response.statusCode !== 200) {
      process.exit(1);
    } else {
      try {
        const movieData = JSON.parse(body);
        if (movieData.characters && movieData.characters.length > 0) {
          movieData.characters.forEach((charUrl) => {
            request(charUrl, (charError, charResponse, charBody) => {
              if (charError) { process.exit(1); } else if (charResponse.statusCode !== 200) { process.exit(1); } else {
                const charData = JSON.parse(charBody);
                console.log(charData.name);
              }
            });
          });
        }
      } catch (e) {
        process.exit(1);
      }
    }
  }

);
