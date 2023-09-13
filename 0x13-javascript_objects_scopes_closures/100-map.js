#!/usr/bin/node
const data = require('./100-data');
const newList = data.list.map((value, index) => value * index);
console.log(data.list);
console.log(newList);
