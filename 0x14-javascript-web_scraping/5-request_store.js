#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) { process.exit(1); } else if (response.statusCode !== 200) { process.exit(1); } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) { process.exit(1); }
    });
  }
}
);
