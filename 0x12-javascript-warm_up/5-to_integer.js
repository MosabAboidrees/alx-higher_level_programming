#!/usr/bin/node
// process.argv is an array containing the command line arguments
const args = process.argv;
// first argument is at index 2
const firstArg = args[2];
// convert the first argument to an integer
const convertedInt = parseInt(firstArg, 10);
if (isNaN(convertedInt)) {
  // if the first argument is not a number, print 'Not a number'
  console.log('Not a number');
} else {
  // if the first argument is a number, print 'My number: ' followed by the number
  console.log('My number: ' + convertedInt);
}
