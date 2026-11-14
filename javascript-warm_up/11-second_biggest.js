#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2);
  parseInt(argv);
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
