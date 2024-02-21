#!/usr/bin/node
const fts = require('fts');
fts.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
