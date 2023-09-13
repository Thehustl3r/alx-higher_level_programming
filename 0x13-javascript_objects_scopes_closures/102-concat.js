#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 3) {
  process.exit(1);
}
const file1 = process.argv[2];
const file2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(file1, 'utf8', (err1, data1) => {
  if (err1) {
    process.exit(1);
  }
  fs.readFile(file2, 'utf8', (err2, data2) => {
    if (err2) {
      process.exit(1);
    }
    const conct = data1 + data2;
    fs.writeFile(destinationFile, conct, (err3) => {
      if (err3) {
        process.exit(1);
      }
    });
  });
});
