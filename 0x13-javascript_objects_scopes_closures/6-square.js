#!/usr/bin/node
// Import the Square class from 5-square.js
const PrevSquare = require('./5-square');

// Define a class Square that inherits from PrevSquare
class Square extends PrevSquare {
  // Define an instance method charPrint that prints the square using the character c
  charPrint (c) {
    // If c is undefined, use the character 'X'
    const char = c === undefined ? 'X' : c;
    // Loop through each row
    for (let i = 0; i < this.height; i++) {
      // Print a row of the square using 'char' repeated width times
      console.log(char.repeat(this.width));
    }
  }
}
// Export the Square class to make it visible from outside
module.exports = Square;
