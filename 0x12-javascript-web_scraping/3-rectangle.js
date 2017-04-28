#!/usr/bin/node

module.exports = {
  Rectangle: function (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function print() {
      row = '';
      for (let i = 0; i < this.width; i++) {
        row = row.concat('X');
      }
      for (let i = 0; i < this.height; i++) {
	console.log(row);
      }
    }
  }
};
