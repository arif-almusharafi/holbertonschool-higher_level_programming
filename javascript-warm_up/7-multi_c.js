#!/usr/bin/node
const { argv } = require('node:process');
const value = parseInt(argv[2]);
const string = 'C is fun';
if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < value; i++) {
    console.log(string);
  }
}
