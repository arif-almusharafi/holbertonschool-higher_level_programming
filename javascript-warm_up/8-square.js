#!/usr/bin/node
const { argv } = require('node:process');
const value = parseInt(argv[2]);
if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    let row = '';
    for (let j = 0; j < value; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
