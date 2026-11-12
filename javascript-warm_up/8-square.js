#!/usr/bin/node
const { argv } = require('node:process');
const value = parseInt(argv[2]);
const string = 'X';
if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    for (let j = 0; j <= value; j++) {
        console.log(string);
    }
  }
}
