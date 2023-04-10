#!/usr/bin/node

const b = Math.floor(Number(process.argv[2]));

if (isNaN(b)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < b; i++) {
    let square = '';
    for (let j = 0; j < b; j++) {
      square = square + 'X';
    }
    console.log(square);
  }
}
