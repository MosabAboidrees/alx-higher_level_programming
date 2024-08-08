// Use the jQuery API to handle the click event on the DIV#toggle_header
$('DIV#toggle_header').click(function() {
  // Check the current class of the <header> element and toggle between 'red' and 'green'
  if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  } else {
    $('header').removeClass('green').addClass('red');
  }
});
