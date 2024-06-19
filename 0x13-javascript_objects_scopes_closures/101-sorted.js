#!/usr/bin/node
// This is the shebang line to specify the interpreter for the script

// Import the dictionary from the 101-data.js file
const dict = require('./101-data').dict;

// Initialize an empty object to hold the new dictionary
const newDict = {};

// Loop through each entry in the original dictionary
for (const userId in dict) {
  // Get the number of occurrences for the current user ID
  const occurrences = dict[userId];

  // If the occurrences value is not yet a key in the new dictionary, add it
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }

  // Add the current user ID to the list of user IDs for the current occurrences value
  newDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(newDict);
