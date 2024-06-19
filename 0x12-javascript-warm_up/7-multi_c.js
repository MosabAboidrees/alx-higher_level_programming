#!/usr/bin/node
// Get the arguments passed to the script, including the default ones
const args = process.argv;
// Convert the first argument to an integer
const x = parseInt(args[2], 10);
// Check if the conversion to integer was not successful (NaN)

if (isNaN(x)) {
  // Print the error message
  console.log('Missing number of occurrences');
} else {
  // If the conversion was successful
  for (let i = 0; i < x; i++) {
    // Print "C is fun" in each iteration
    console.log('C is fun');
  }
}
