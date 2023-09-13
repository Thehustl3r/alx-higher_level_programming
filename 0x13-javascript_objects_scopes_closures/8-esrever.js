#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let i = list.length; i > 0; i--) {
    newlist.push(list[i - 1]);
  }
  return newlist;
};
