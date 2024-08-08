// Use the jQuery API to fetch data from the URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  // Iterate over the results and append each movie title to the UL#list_movies
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
