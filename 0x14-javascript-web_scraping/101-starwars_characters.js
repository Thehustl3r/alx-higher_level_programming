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
		const charUrls = movieData.characters;

		const fetchCharacter = (index) => {

			if (index < characterUrls.length){

				request(

					charUrls[index],
					(charError, charResponse, charBody) => {

						if (charError)
							process.exit(1);
						else if (charResponse.statusCode !== 200)
							process.exit(1);
						else {

							const charData = JSON.parse(charBody);
							console.log(charData.name);

							// Fetch the next character
							fetchCharacter(index + 1);
						}
					}
				);
			
			}
		};
		fetchCharacter(0);
          }else{
		  process.exit(1);
        }
      } catch (e) {
        process.exit(1);
      }
    }
  }

);
