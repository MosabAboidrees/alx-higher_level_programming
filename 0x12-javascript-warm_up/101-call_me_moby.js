// Define a function that executes another function x times
function callMeMoby(x, theFunction) {
	// Loop x times
	for (let i = 0; i < x; i++) {
	  // Execute the provided function
	  theFunction();
	}
  }

  // Export the callMeMoby function to make it visible from outside
  module.exports.callMeMoby = callMeMoby;
