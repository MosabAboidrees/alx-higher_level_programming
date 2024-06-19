#!/usr/bin/node
// This is the shebang line to specify the interpreter for the script

// Define an object with type and value properties
const myObject = {
  type: 'object',
  value: 12
};

// Print the object before modification
console.log(myObject);

/*
YOUR CODE HERE
*/
// Add a new function incr to the object that increments the value property
myObject.incr = function () {
  this.value++;
};

// Call the incr function to increment the value and print the object
myObject.incr();
console.log(myObject);

// Call the incr function again to increment the value and print the object
myObject.incr();
console.log(myObject);

// Call the incr function one more time to increment the value and print the object
myObject.incr();
console.log(myObject);
