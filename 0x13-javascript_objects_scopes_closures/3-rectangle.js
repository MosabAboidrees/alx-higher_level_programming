#!/usr/bin/node
// Define a class Rectangle
class Rectangle {
  // Constructor that takes 2 arguments: w and h
  constructor (w, h) {
    // Check if w and h are positive integers greater than 0
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      // Initialize the instance attribute width with the value of w
      this.width = w;
      // Initialize the instance attribute height with the value of h
      this.height = h;
    }
  }

  // Define an instance method print that prints the rectangle using the character X
  print () {
    // Loop through each row
    for (let i = 0; i < this.height; i++) {
      // Print a row of the rectangle using 'X' repeated width times
      console.log('X'.repeat(this.width));
    }
  }
}
// Export the Rectangle class to make it visible from outside
module.exports = Rectangle;
