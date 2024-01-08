#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
	console.log("Missing number of occurance");
} else {
	for (let a = 0; a < x; a++) {
		console.log("C is fun");
	}
}
