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
}
// Export the Rectangle class to make it visible from the outside
module.exports = Rectangle;
