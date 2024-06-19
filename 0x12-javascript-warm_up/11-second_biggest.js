#!/usr/bin/node
// Get the arguments passed to the script, including the default ones
const args = process.argv;
// Check if there are less than 3 arguments (i.e., no user arguments or only one argument)
if (args.length <= 3) {
  // Print 0 if there are less than 3 arguments
  console.log(0);
} else {
  // Convert arguments to integers and store them in an array
  const integers = args.slice(2).map(Number);
  // Sort the array in descending order
  integers.sort((a, b) => b - a);
  // Print the second biggest integer
  console.log(integers[1]);
}
