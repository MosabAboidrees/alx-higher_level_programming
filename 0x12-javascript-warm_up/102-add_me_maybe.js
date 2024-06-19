#!/usr/bin/node
// Define a function that increments a number and calls another function
function addMeMaybe (number, theFunction) {
  // Increment the number by 1
  const incrementedNumber = number + 1;
  // Call the provided function with the incremented number
  theFunction(incrementedNumber);
}
// Export the addMeMaybe function to make it visible from outside
module.exports.addMeMaybe = addMeMaybe;
