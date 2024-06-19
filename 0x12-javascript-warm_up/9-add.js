#!/usr/bin/node
// Get the arguments passed to the script, including the default ones
const args = process.argv;
// Convert the first argument to an integer
const a = parseInt(args[2], 10);
// Convert the second argument to an integer
const b = parseInt(args[3], 10);
// Define a function to add two numbers
function add (a, b) {
  return a + b;
}
// Print the result of the addition, or NaN if arguments are not numbers
console.log(add(a, b));
