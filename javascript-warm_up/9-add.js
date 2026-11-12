#!/usr/bin/node
const { argv } = require('node:process');

const a = argv[2];
const b = argv[3];
function add (a, b) {
  return(a + b);
}

console.log(add(a,b));
