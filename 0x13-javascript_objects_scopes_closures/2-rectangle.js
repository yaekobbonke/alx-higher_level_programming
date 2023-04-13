#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h <= 0) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
