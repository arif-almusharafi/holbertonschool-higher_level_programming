#!/usr/bin/node
const { argv } = require('node:process');
function Factorial (x) {
  if (isNaN(x) || x <= 0) {
    return (1);
  }
  return (x * Factorial(x - 1));
}

console.log(Factorial(parseInt(argv[2])));
