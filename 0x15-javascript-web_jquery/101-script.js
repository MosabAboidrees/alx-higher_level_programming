$(document).ready(function() {
  // Handle the click event on DIV#add_item to add a new <li> element
  $('DIV##add_item').click(function() {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Handle the click event on DIV#remove_item to remove the last <li> element
  $('DIV##remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });

  // Handle the click event on DIV#clear_list to remove all <li> elements
  $('DIV##clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
