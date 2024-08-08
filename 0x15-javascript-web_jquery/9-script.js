// Use the jQuery API to ensure the DOM is fully loaded before running the script
$(document).ready(function() {
  // Use the jQuery API to fetch data from the URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Display the value of "hello" in the DIV#hello
    $('DIV#hello').text(data.hello);
  });
});
