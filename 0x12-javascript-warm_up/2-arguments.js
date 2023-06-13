#!/usr/bin/node
const n = process.argv.length;
console.log(n === 2 ? 'No Argument' : n === 3 ? 'Argument found' : 'Arguments found');
