#!/usr/bin/node
// Get the arguments passed to the script, including the default ones
const args = process.argv;
// Convert the first argument to an integer
const n = parseInt(args[2], 10);
// Define a function to compute the factorial recursively
function factorial (n) {
  // If n is NaN or less than 0, return 1
  if (isNaN(n) || n <= 0) {
    return 1;
  }
  // Base case: if n is 1, return 1
  if (n === 1) {
    return 1;
  }
  // Recursive case: n times the factorial of n-1
  return n * factorial(n - 1);
}
// Print the result of the factorial computation
console.log(factorial(n));
