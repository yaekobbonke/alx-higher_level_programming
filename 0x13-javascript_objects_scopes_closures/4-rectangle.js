#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let size = 0; size < this.height; size++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
