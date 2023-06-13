#!/usr/bin/node
const args = process.argv;
console.log(typeof args === 'undefined' ? 'No argument' : args[2]);
