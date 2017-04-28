#!/usr/bin/node

const Rectangle = require('./4-rectangle').Rectangle;

module.exports = {
  Square: function (size) {
    Rectangle.call(this, size, size);
  }
};
