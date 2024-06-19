#!/usr/bin/node

// Get the arguments passed to the script, including the default ones
const args = process.argv;

// Convert the first argument to an integer to determine the size of the square
const size = parseInt(args[2], 10);

// Check if the conversion to integer was not successful (NaN)
if (isNaN(size)) {
  // Print "Missing size" if the conversion was not successful
  console.log('Missing size');
} else {
  // The conversion to integer was successful
  // Loop to print each row of the square
  for (let i = 0; i < size; i++) {
    // Print a row of the square using 'X' repeated 'size' times
    console.log('X'.repeat(size));
  }
}
