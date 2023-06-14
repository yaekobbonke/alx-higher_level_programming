#!/usr/bin/node
exports.nbOccurences = function (list, element) {
  return list.filter((n) => n === element).length;
};
