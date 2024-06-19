#!/usr/bin/node

const args = process.argv; // Get the arguments
const firstArg = args[2]; // Get the first argument
const secondArg = args[3]; // Get the second argument
// Print the first and second arguments in the format "firstArg is secondArg"
// If the second argument is not provided, print 'undefined'
console.log(firstArg + ' is ' + (secondArg || 'undefined'));
