#!/usr/bin/node
const dict = require('./101-data');
const newDict = {};
for (const key in dict.dict) {
  const occurence = dict.dict[key];
  if (newDict[occurence] === undefined) {
    newDict[occurence] = [key];
  } else {
    newDict[occurence].push(key);
  }
}
console.log(newDict);
