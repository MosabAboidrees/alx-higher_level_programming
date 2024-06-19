#!/usr/bin/node
// Import the Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Define a class Square that inherits from Rectangle
class Square extends Rectangle {
  // Constructor that takes 1 argument: size
  constructor (size) {
    // Call the constructor of Rectangle with size as both width and height
    super(size, size);
  }
}
// Export the Square class to make it visible from outside
module.exports = Square;
