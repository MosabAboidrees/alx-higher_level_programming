#!/usr/bin/node
// Script to write a string to a file

const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

if (filePath === undefined) {
  console.error('Error: No file path provided');
  process.exit(1);
}

fs.writeFile(filePath, fileContent || '', 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
