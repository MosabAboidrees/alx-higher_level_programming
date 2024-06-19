#!/usr/bin/node
// Define a function that converts a number from base 10 to another base passed as argument
exports.converter = function (base) {
  // Return a function that converts a number to the specified base
  return function (number) {
    // Convert the number to the specified base and return the result
    return number.toString(base);
  };
};
