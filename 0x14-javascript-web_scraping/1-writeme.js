#!/usr/bin/node
const s = require('s');
s.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
