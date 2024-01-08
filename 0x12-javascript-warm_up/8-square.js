#!/usr/bin/node

const t_size = Math.floor(Number(process.argv[2]));
if (isNaN(t_size)) {
	console.log("Missing size");
} else {
	for (let r = 0; r < t_size; r++) {
		let row = '';
		for (let c = 0; c < t_size; c++) row += 'X';
		console.log(row);
	}
}
