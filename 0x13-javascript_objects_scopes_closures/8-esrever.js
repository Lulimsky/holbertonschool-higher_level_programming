#!/usr/bin/node

exports.esrever = function (list) {
  const array = [];
  while (list.length) {
    array.push(list.pop());
  }
  return array;
};
