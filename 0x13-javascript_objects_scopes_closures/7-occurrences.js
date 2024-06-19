#!/usr/bin/node
// Define a function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter to keep track of occurrences
  let count = 0;

  // Loop through each element in the list
  for (let i = 0; i < list.length; i++) {
    // If the current element matches the search element, increment the counter
    if (list[i] === searchElement) {
      count++;
    }
  }
  // Return the total count of occurrences
  return count;
};
