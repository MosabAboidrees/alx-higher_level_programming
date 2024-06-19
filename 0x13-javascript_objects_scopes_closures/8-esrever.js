#!/usr/bin/node
// Define a function that returns the reversed version of a list
exports.esrever = function (list) {
  // Initialize an empty array to hold the reversed list
  const reversedList = [];

  // Loop through the original list from end to start
  for (let i = list.length - 1; i >= 0; i--) {
    // Push each element into the reversed list
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
