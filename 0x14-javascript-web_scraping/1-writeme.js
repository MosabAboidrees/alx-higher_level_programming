#!/usr/bin/node
// Script to write a string to a file

const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

if (!filePath || !fileContent) {
  console.error('Error: Missing arguments');
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

fs.writeFile(filePath, fileContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
