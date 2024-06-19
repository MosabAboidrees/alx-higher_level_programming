#!/usr/bin/node
// This is the shebang line to specify the interpreter for the script

const args = process.argv.slice(2);
// Get the arguments passed to the script, excluding the first two default arguments

if (args.length === 0) {
  // Check if no arguments are passed
  console.log('No argument');
  // Print "No argument" if no arguments are passed
} else if (args.length === 1) {
  // Check if exactly one argument is passed
  console.log('Argument found');
  // Print "Argument found" if one argument is passed
} else {
  // More than one argument is passed
  console.log('Arguments found');
  // Print "Arguments found" if more than one argument is passed
}
