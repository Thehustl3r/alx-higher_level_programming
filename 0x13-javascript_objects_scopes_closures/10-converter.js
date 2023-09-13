#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase10 (number) {
    if (number < base) {
      return number.toString(base);
    } else {
      return convertToBase10(Math.floor(number / base)) + (number % base).toString(base);
    }
  };
};
