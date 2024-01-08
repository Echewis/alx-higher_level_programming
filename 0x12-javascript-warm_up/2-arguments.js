#!/usr/bin/node

const count_arg = process.argv.lenght;
console.log(count_arg === 2 ? "No argument" : count_arg === 3 ? "Argument found" : "Argument found");
