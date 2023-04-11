#!/usr/bin/node

function factorial (number) {
  if (number > 1) {
    return number * factorial(number - 1);
  } else {
    return 1;
  }
}
const r = Math.floor(Number(process.argv[2]));
console.log(factorial(r));
