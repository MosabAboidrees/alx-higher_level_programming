#!/usr/bin/node
// This is the shebang line to specify the interpreter for the script

// Import the list from the 100-data.js file
const list = require('./100-data').list;

// Print the initial list
console.log(list);

// Create a new list with each value equal to the value
// of the initial list multiplied by the index in the list
const newList = list.map((value, index) => value * index);

// Print the new list
console.log(newList);
