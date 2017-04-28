#!/usr/bin/node

const Rectangle = require('./4-rectangle').Rectangle;

module.exports = {
  Square: function (size) {
    Rectangle.call(this, size, size);
    this.charPrint = function (c) {
      if (c === undefined) {
        c = 'X';
      }
      let row = '';
      for (let i = 0; i < size; i++) {
        row = row.concat(c);
      }
      for (let i = 0; i < size; i++) {
        console.log(row);
      }
    };
  }
};
