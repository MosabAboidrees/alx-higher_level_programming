#!/usr/bin/node

// Define a function that returns the addition of two integers
function add (a, b) {
  return a + b;
}

// Export the add function to make it visible from outside
module.exports = { add };

// Get the arguments passed to the script, including the default ones
const args = process.argv.slice(2);

// Convert the first argument to an integer
const a = parseInt(args[0], 10);

// Convert the second argument to an integer
const b = parseInt(args[1], 10);

// Print the result of the addition
console.log(add(a, b));
