// Use the jQuery API to fetch data from the URL
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  // Display the character name in the DIV#character
  $('DIV#character').text(data.name);
});
