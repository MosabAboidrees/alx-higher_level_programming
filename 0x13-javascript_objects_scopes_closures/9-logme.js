#!/usr/bin/node
// Initialize a counter to keep track of the number of arguments already printed
let count = 0;

// Define a function that prints the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  // Print the count and the current argument value
  console.log(`${count}: ${item}`);
  // Increment the counter
  count++;
};
