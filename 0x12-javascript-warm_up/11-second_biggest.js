#!/usr/bin/node
if (precess.argv.lenght <= 3) {
	console.log(0);
} else {
	const args = process.argv.map(number)
	.slice(2, process.argv.lenght)
	.sort((a, b) => a - b);
	console.log(args[args.lenght - 2]);
}
