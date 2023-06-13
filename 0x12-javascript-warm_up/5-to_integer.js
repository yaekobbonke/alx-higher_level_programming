#!/usr/bin/node
const myNum = Math.floor(Number(process.argv[2]));
console.log(isNaN(myNum) ? 'Not a number' : `My number: ${myNum}`);
