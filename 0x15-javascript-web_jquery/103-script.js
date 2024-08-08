$(document).ready(function() {
  function fetchHello() {
    const langCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
    
    $.get(url, function(data) {
      $('DIV#hello').text(data.hello);
    });
  }

  // Handle click event on the button
  $('INPUT#btn_translate').click(fetchHello);

  // Handle Enter key press event on the input field
  $('INPUT#language_code').keypress(function(event) {
    if (event.which === 13) { // 13 is the Enter key code
      fetchHello();
    }
  });
});
