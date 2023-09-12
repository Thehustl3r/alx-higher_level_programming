#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    super.x = c === undefined ? 'x' : c;
    super.print();
  }
}
module.exports = Square;
