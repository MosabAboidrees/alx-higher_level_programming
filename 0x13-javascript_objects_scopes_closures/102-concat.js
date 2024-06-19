#!/usr/bin/node
// This is the shebang line to specify the interpreter for the script

// Import the required modules
const fs = require('fs');

// Get the file paths from the command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Read the content of the first source file
const contentA = fs.readFileSync(fileA, 'utf8');

// Read the content of the second source file
const contentB = fs.readFileSync(fileB, 'utf8');

// Concatenate the content of the two source files
const contentC = contentA + contentB;

// Write the concatenated content to the destination file
fs.writeFileSync(fileC, contentC);
