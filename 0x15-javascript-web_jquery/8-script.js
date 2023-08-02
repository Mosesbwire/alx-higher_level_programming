const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$(document).ready(()=>{
	const ul = $('#list_movies');
	$.get(URL, (data, status)=>{
		if (status === 'success'){
			data.results.forEach(movie =>{
				ul.append(`<li>${movie['title']}</li>`);
			});
		}
	});
});
