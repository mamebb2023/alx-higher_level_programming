#!/usr/bin/node
function factorial (n) {
  if (n === NaN || n === 0) return 1;
  return n * factorial(n - 1);
}

const n = process.argv[2];
console.log(factorial(Number(n)));
