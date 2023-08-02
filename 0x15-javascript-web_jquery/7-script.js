const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$(document).ready(()=>{
	$.get(URL, (data, status)=> {
		
		if (status === 'success'){
			$('#character').text(data["name"]);
		}
	});
});
