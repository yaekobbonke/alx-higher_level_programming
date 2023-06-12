#!/usr/bin/node
let string;
if (process.argv.length < 3) {
  string = 'No argument';
} else if (process.argv.length === 3) {
  string = 'Argument found';
} else {
  string = 'Arguments found';
}
console.log(string);
