#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
	charprint (d) {
		if (d === undefined) {
			this.print();
		} else {
			for (let a = 0; a < this.height; a++) console.log(d.repeat(this.width));
		}
	}
};
