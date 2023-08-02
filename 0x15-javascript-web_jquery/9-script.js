const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
const settings = {
"cache": false,
"dataType": "jsonp",
"async": true,
"crossDomain": true,
"url": URL,
"method": "GET",
"headers": {
		"accept": "application/json",
		"Access-Control-Allow-Origin":"*"
	}
};


$(document).ready(()=> {
	console.log('doc is ready');
	$.ajax(settings).done((res)=>{
		console.log(res);
	})
});
