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

  // Define an instance method rotate that exchanges the width and height of the rectangle
  rotate () {
    // Swap the values of width and height
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Define an instance method double that multiplies the width and height of the rectangle by 2
  double () {
    // Double the values of width and height
    this.width *= 2;
    this.height *= 2;
  }
}
// Export the Rectangle class to make it visible from outside
module.exports = Rectangle;
