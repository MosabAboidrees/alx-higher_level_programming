// Use the jQuery API to handle the click event on the DIV#add_item
$('DIV#add_item').click(function() {
  // Add a new <li> element with the text 'Item' to the <ul> with the class 'my_list'
  $('ul.my_list').append('<li>Item</li>');
});
