#!/usr/bin/node
const myNumber = parseInt(process.argv[2]);
if (isNaN(myNumber)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNumber; i++) {
    let row = '';
    for (let j = 0; j < myNumber; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
