#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    process.exit(1);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
}
);
